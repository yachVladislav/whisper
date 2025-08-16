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
- docker-compose up -d
3. **Download the LLM model (first run only)**
- docker exec -it ollama ollama pull llama3:1b