from dataclasses import dataclass

@dataclass
class ASRResult:
    text: str
    lang: str
    duration: float

@dataclass
class LLMResult:
    request_id: str
    status: str
    text: str = ''
    answer: str = ''
    error: str = ''