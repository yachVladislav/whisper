import subprocess
from pathlib import Path
import tempfile

def preprocess_audio(input_path: str) -> str:
    temp_wav = Path(tempfile.mktemp(suffix=".wav"))
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        "-af", "loudnorm",
        "-sample_fmt", "s16",
        str(temp_wav)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return str(temp_wav)
