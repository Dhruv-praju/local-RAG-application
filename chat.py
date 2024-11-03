## 1. Load, Split and Store documents in Vector database

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Amazon_Web_Services")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
all_splits = text_splitter.split_documents(data)

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

# create model for embedding of vector store
local_embeddings = OllamaEmbeddings(model="nomic-embed-text")

# create a vector store containing embeddings of all documents
vectorstore = Chroma.from_documents(documents=all_splits, embedding=local_embeddings)

print('Successfully stored documents in VectorDB!!')

## 2. Load LLM model

from langchain_ollama import ChatOllama

model = ChatOllama(
    model="smollm:135m",
)

print('Successfully loaded LLM!')

## 3.  RAG implementation 

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from datetime import datetime

# Convert loaded documents into strings by concatenating their content and ignoring metadata
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

from langchain_core.prompts import ChatPromptTemplate

# Create the prompt template
RAG_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise, short.

<context>
{context}
</context>

Answer the following question:

{question}"""

prompt = ChatPromptTemplate.from_template(RAG_TEMPLATE)

# Create the llm chain with the prompt template
chain = (
    RunnablePassthrough.assign(context=lambda input: format_docs(input["context"]))
    | prompt
    | model
)


# Chatbot interface
from datetime import datetime

print("\nHello, how are you? I'm XYZ bot.\n")

while True:
    current_date = datetime.now()
    user_input = input("I'm here to assist you. Ask me something about AWS. To exit, type 'q': ")

    if user_input.lower() == "q":
        print("\nExiting. Have a great day!\n")
        break

    # Perform a similarity search in the vector database
    docs = vectorstore.similarity_search(user_input)
    
    # Generate a response using the language model
    resp = chain.invoke(
        {
            "question": user_input,
            "context": docs,
            "current_date": current_date,
        }
    )
    
    print("\nXYZ bot: ", resp.content)
    print("\n______________________________________________________\n")



print('Sucessfully implemented RAG!!')

# cleanup
vectorstore.delete_collection()