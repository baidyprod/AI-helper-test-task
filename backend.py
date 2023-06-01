import os
from datetime import datetime

from dotenv import load_dotenv

from init_db import index_name

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain.vectorstores import Pinecone

import pinecone

import pytz


load_dotenv()

pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT_REGION'))


def get_current_weekday_ukrainian():
    dates_translation = {
        "Monday": "понеділок",
        "Tuesday": "вівторок",
        "Wednesday": "середа",
        "Thursday": "четвер",
        "Friday": "п'ятниця",
        "Saturday": "субота",
        "Sunday": "неділя",
    }

    target_timezone = pytz.timezone('Europe/Kyiv')
    current_time = datetime.now(pytz.utc).astimezone(target_timezone)
    english_date = current_time.strftime("%A")
    return dates_translation[english_date]


_template = """Given the following conversation and a follow up question with current weekday. Rephrase the follow up question to be a standalone question, in its original language. Add a current weekday if needed.

Conversation:
{chat_history}
Follow Up Question: {question}""" + f"""
Current Weekday: {get_current_weekday_ukrainian()}
""" + """Standalone question:"""  # noqa: E501

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)


def run_llm(query, chat_history):
    embeddings = OpenAIEmbeddings()
    vectordb = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectordb.as_retriever(), condense_question_prompt=CONDENSE_QUESTION_PROMPT
    )
    return qa({"question": query, "chat_history": chat_history})
