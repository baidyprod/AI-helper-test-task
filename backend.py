import locale
from datetime import datetime

from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

locale.setlocale(locale.LC_TIME, "uk_UA")


def run_llm(query, chat_history):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    qa = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectordb.as_retriever())
    return qa(
        {
            "question": query + " Якщо для твоєї відповіді це потрібно, то сьогодні " + datetime.now().strftime("%A"),
            "chat_history": chat_history,
        }
    )
