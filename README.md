# whisper
FastAPI audio processing service: takes a voice message, sends it to GenAI to convert it to text and generate a response, then returns the result as text. Uses FastAPI and ASR + NLP models.

### Prerequisites
- Docker and Docker Compose installed  
- (Optional) Git (if cloning the repository)  

### Installation & Running

1. **Clone the repository**
- git clone link-repo
- cd your-repo
2. **Start services**
- docker-compose up -d --build
3. **Download the LLM model (first run only)**
- docker exec -it ollama ollama pull llama3.2:1b

## Warning
When you **run the app for the first time** the Whisper model is loaded, which may take some time (depending on your internet connection speed and system performance). Please wait until this process is complete.

The FastAPI server will only start working after the model is fully loaded. You can determine whether the server is ready by the message in the logs:

Uvicorn running on http://0.0.0.0:8000 

## Using the API

Once the server is running, you can interact with the API via:

1. **Swagger UI** (interactive documentation):

Open in your browser: [http://localhost:8000/docs](http://localhost:8000/docs)

Here you can:
- See all available endpoints
- Test the API directly from your browser
- View sample requests and responses