import os
import mimetypes


class FileManager:
    """Manage file-related operations."""

    @staticmethod
    def exists(file_path: str) -> bool:
        return os.path.exists(file_path)

    @staticmethod
    def determine_file_type(file_path: str) -> str:
        """
        Determine the file type (audio or video) based on MIME type or file extension.
        Raises an error if the type cannot be determined.
        """
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type:
            if mime_type.startswith("audio"):
                return "audio"
            if mime_type.startswith("video"):
                return "video"
        else:
            # Fallback: check extension if mimetype is None.
            ext = os.path.splitext(file_path)[1].lower()
            if ext in {".mp3", ".wav", ".flac", ".aac"}:
                return "audio"
            if ext in {".mp4", ".mkv", ".avi", ".mov"}:
                return "video"

        raise ValueError(
            f"Could not determine file type for {file_path}. Please provide a file with a valid audio or video extension."
        )

    @staticmethod
    def ensure_converted_folder() -> str:
        """Ensure the 'converted' folder exists and return its path."""
        converted_folder = os.path.join(os.getcwd(), "converted")
        os.makedirs(converted_folder, exist_ok=True)
        return converted_folder
