from abc import ABC, abstractmethod
from domain.models import ASRResult, LLMResult


class IASR(ABC):
    @abstractmethod
    def transcribe(self, audio_path: str) -> ASRResult:
        pass

class ILLM(ABC):
    @abstractmethod
    def generate(self, text: str) -> LLMResult:
        pass

class IStorage(ABC):
    @abstractmethod
    def save_file(self, file_bytes: bytes, filename: str) -> str:
        pass