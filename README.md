# Description
This project is a RAG application running with local quantized LLM called "smollm" with 135M parameters. I have use [Ollama](https://github.com/ollama/ollama) which is a platform for running and managing large language models (LLMs) on local machine. The application runs entirely on Laptop and can interact via command line.
This chatbot answers any questions based on this [AWS Wikipedia page](https://en.wikipedia.org/wiki/Amazon_Web_Services). You can replace it with any webpage link based on which you want answers from the chatbot. 


### RAG Architecture Implementation:
**Storage**:

It ingests the data from the source and stores it in Vector Database. I have used Vector Database as **chromaDB**.

1. Load: First we need to load our data. This is done with Document Loaders. I have used AWS wikipedia page as the data.
2. Split: Text splitters break large Documents into smaller chunks. 
3. Store: We need somewhere to store and index our splits, so that they can be searched over later. This is often done using a VectorStore and Embeddings model.
![alt text](image-1.png)

**Retrieval and generation**

It Retrives the relevant context from the vectorDB and passes it to LLM

4. Retrieve: Given a user input, relevant splits of the document are retrieved from VectorStore using a Retriever.
5. Generate: A LLM produces a response using a prompt that includes both the question with the retrieved data.
![alt text](image-2.png)
# Set up the Environment

```
### Run vectorDB 'chromadb' on localhost:9000
docker run -d -p 9000:8000 --name chromadb chromadb/chroma

### Run ollama server on localhost:11434
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

## download model and embedding from the ollama server
docker exec -it ollama ollama pull nomic-embed-text
docker exec -it ollama ollama pull smollm:135m
```

# Download libararies and Run CLI ChatBot
```
pip install -r requirements.txt

python chat.py
```


