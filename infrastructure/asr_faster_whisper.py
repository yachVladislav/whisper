from faster_whisper import WhisperModel
from domain.models import ASRResult
from .audio_utils import preprocess_audio
from domain.interfaces import IASR


class FasterWhisperASR(IASR):
    def __init__(self):
        self.model = WhisperModel("small", device="cpu", compute_type="int8", download_root="/storage")

    def transcribe(self, audio_path: str) -> ASRResult:
        processed_path = preprocess_audio(audio_path)
        segments, info = self.model.transcribe(processed_path)
        text = " ".join([segment.text for segment in segments])
        return ASRResult(text=text.strip(), lang=info.language, duration=info.duration)
