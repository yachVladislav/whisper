from pathlib import Path
from domain.interfaces import IStorage


class LocalStorage(IStorage):
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save_file(self, file_bytes: bytes, filename: str) -> str:
        dest = self.base_path / filename
        with open(dest, "wb") as f:
            f.write(file_bytes)
        return str(dest)