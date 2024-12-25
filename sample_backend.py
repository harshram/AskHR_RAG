#1. Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_aws import BedrockEmbeddings

from langchain_community.vectorstores import FAISS

from langchain.indexes.vectorstore import VectorstoreIndexCreator

from langchain_aws import BedrockLLM
 
#5c. Wrap within a function
def hr_index():
    #2. Define the data source and load data with PDFLoader(https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf)
   
    data_load = PyPDFLoader("https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf")
    #3. Split the Text based on Character, Tokens etc. - Recursively split by character - ["\n\n", "\n", " ", ""]
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""],chunk_size=100,chunk_overlap=10)
    #4. Create Embeddings -- Client connection
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name ="bedrock_rag",
        model_id="amazon.titan-embed-text-v1"
    )
    #5à Create Vector DB, Store Embeddings and Index for Search - VectorstoreIndexCreator
    index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding= data_embeddings,
        vectorstore_cls=FAISS

    )
    #5b  Create index for HR Policy Document

    db_index = index.from_loaders([data_load])
   
    return db_index

    #6a. Write a function to connect to Bedrock Foundation Model - Claude Foundation Model

def hr_llm():

    model = BedrockLLM(
        credentials_profile_name='default',
        model_id= 'meta.llama3-70b-instruct-v1:0',
        model_kwargs= 
        {
            "temperature"=0.1,
            "top_p"=0.9
        }
    )
    return model



#6b. Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM.

def hr_rag_response(index,question):

    data_model = hr_llm()
    response = index.query(question=question,llm=data_model)

    return response







# Index creation --> https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html
