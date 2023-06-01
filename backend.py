from datetime import datetime

from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain.vectorstores import Chroma

load_dotenv()


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
    english_date = datetime.now().strftime("%A")
    return dates_translation[english_date]


_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.

Chat History:
{chat_history}
Follow Up Input: {question}""" + f"""
Current weekday: {get_current_weekday_ukrainian()}
""" + """Standalone question:"""  # noqa: E501

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)


def run_llm(query, chat_history):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectordb.as_retriever(), condense_question_prompt=CONDENSE_QUESTION_PROMPT
    )
    return qa({"question": query, "chat_history": chat_history})
