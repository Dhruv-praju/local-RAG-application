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

# Run CLI ChatBot
`python chat.py`


https://github.com/ollama/ollama