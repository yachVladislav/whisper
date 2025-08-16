from fastapi import APIRouter, UploadFile, File, HTTPException
from application.services import VoicePipelineService
from infrastructure.asr_faster_whisper import FasterWhisperASR
from infrastructure.llm_ollama import OllamaLLM
from infrastructure.storage_local import LocalStorage
import uuid

router = APIRouter()
storage = LocalStorage("/storage")
service = VoicePipelineService(asr=FasterWhisperASR(), llm=OllamaLLM("llama3.2:1b"))

@router.post("/process")
async def process_audio(file: UploadFile = File(...)):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(400, detail="Файл должен быть аудио")

    request_id = str(uuid.uuid4())
    content = await file.read()
    saved_path = storage.save_file(content, f"{request_id}__{file.filename}")
    result = service.process_audio(saved_path, request_id)
    return result.__dict__
