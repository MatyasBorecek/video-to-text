import os
import argparse
import torch

from .audio_processor import AudioProcessor
from .file_manager import FileManager
from .result_saver import save_result_to_file
from .speaker_recognition import SpeakerRecognition
from .transcriber import Transcriber


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Process an audio or video file to extract and transcribe audio."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the input audio or video file.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    input_file = args.input_file

    if torch.cuda.is_available():
        print(f"[INFO] CUDA available! Using {torch.cuda.get_device_name(0)}")
    else:
        print("[WARNING] CUDA not available. Whisper will run on CPU, which is slower.")

    try:
        if not FileManager.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' does not exist!")

        file_type = FileManager.determine_file_type(input_file)
        print(f"[INFO] Detected file type: {file_type}")

        # If the file is video, extract audio to the converted folder.
        if file_type == "video":
            converted_folder = FileManager.ensure_converted_folder()
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            audio_file = os.path.join(converted_folder, f"{base_name}.mp3")

            if not FileManager.exists(audio_file):
                print(f"[INFO] Extracting audio from video '{input_file}'...")
                AudioProcessor.extract_audio(input_file, audio_file)
            else:
                print(f"[INFO] Audio file '{audio_file}' already exists. Skipping extraction.")

        # If the file is audio, simply use it.
        elif file_type == "audio":
            audio_file = input_file
            print(f"[INFO] Processing audio file '{audio_file}'.")

        else:
            raise ValueError("Unsupported file type.")

        transcriber = Transcriber()
        transcribed_text = transcriber.transcribe_audio(audio_file)

        processed_text = SpeakerRecognition.process_transcription(transcribed_text)
        save_result_to_file(processed_text)

    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
