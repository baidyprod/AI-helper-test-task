from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma

from locations_scraper import scrape_locations

load_dotenv()


def addresses_splitter():
    addresses = scrape_locations()
    res = []
    for key, value in addresses.items():
        d = {key: value}
        res.append(Document(page_content=str(d)))
    return res


def faq_splitter():
    loader = PyPDFLoader("support.pdf")
    res = loader.load_and_split()
    return res


if __name__ == "__main__":
    docs_support = faq_splitter()
    docs_addresses = addresses_splitter()
    docs = docs_support + docs_addresses
    persist_directory = "db"
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
    vectordb.persist()
