import os
import ctypes.util

if os.name == "nt":
    original_find_library = ctypes.util.find_library


    def safe_find_library(name):
        result = original_find_library(name)
        if result is None:
            return "msvcrt.dll"
        return result


    ctypes.util.find_library = safe_find_library

import torch
import whisper
from .file_manager import FileManager


class Transcriber:
    """Transcribe audio to text using the Whisper model."""

    def __init__(self, model_size: str = "small") -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[INFO] Loading Whisper model ({model_size}) on {device}...")
        self.model = whisper.load_model(model_size, device=device)

    def transcribe_audio(self, audio_path: str) -> str:
        print("[INFO] Transcribing audio")
        if not FileManager.exists(audio_path):
            raise FileNotFoundError(f"Audio file '{audio_path}' does not exist!")
        result = self.model.transcribe(audio_path)
        print("[INFO] Transcription completed.")
        return result["text"]
