from domain.models import LLMResult, ASRResult
from infrastructure.asr_faster_whisper import FasterWhisperASR
from infrastructure.llm_ollama import OllamaLLM


class VoicePipelineService:
    def __init__(self, asr: FasterWhisperASR, llm: OllamaLLM):
        self.asr = asr
        self.llm = llm

    def process_audio(self, audio_path: str, request_id: str) -> LLMResult:
        try:
            asr_result: ASRResult = self.asr.transcribe(audio_path)
            answer = self.llm.generate(f"Пользователь сказал: {asr_result.text}")
            return LLMResult(
                request_id=request_id,
                status="done",
                text=asr_result.text,
                answer=answer
            )
        except Exception as e:
            return LLMResult(request_id=request_id, status="error", error=str(e))
