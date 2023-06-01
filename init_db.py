import os

from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Pinecone

from locations_scraper import scrape_locations

import pinecone

load_dotenv()

pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT_REGION'))

index_name = "helper-test-task"


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
    embedding = OpenAIEmbeddings()
    vectordb = Pinecone.from_documents(docs, embedding, index_name=index_name)
