from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, SystemMessage
from domain.interfaces import ILLM
from .prompt import PROMPT


class OllamaLLM(ILLM):
    def __init__(self, model_name: str = "llama3.2:1b", api_url: str = "http://ollama:11434"):
        self.llm = Ollama(model=model_name, base_url=api_url)

    def generate(self, text: str) -> str:
        messages = [
            SystemMessage(content=PROMPT),
            HumanMessage(content=text)
        ]
        return self.llm.invoke(messages)
