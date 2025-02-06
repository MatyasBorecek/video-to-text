import ffmpeg
from .file_manager import FileManager


class AudioProcessor:
    """Extract audio from a video file."""

    @staticmethod
    def extract_audio(video_path: str, audio_path: str = "audio.mp3") -> None:
        if not FileManager.exists(video_path):
            raise FileNotFoundError(f"Video file '{video_path}' does not exist!")
        ffmpeg.input(video_path).output(audio_path, format="mp3").run(overwrite_output=True)
        print(f"[INFO] Audio extracted successfully to {audio_path}.")
