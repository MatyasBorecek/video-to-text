# Video-to-Text Transcription Tool

This project is a command-line tool designed to process video or audio files, extract audio (if necessary), and transcribe it into text using the OpenAI Whisper model. The transcriptions include
simulated speaker diarization.

## Features

- **Audio Extraction**: Automatically extracts audio from video files (e.g., MP4, MKV) and saves it as an MP3 file.
- **Audio Transcription**: Transcribes the extracted or provided audio to text using the Whisper AI model.
- **Speaker Simulation**: Includes simulated speaker diarization, alternating between "Speaker 1" and "Speaker 2."
- **CUDA Support**: Runs on GPU if CUDA is available for faster performance.
- **Output Management**: Saves transcription results to a text file.

## Requirements

- **Python** 3.8+
- **ffmpeg**: Required for audio extraction from video files.
- **CUDA-enabled GPU** (optional): For faster processing with Whisper.

### Python Dependencies:

- **torch**: For processing with CUDA and Whisper.
- **ffmpeg-python**: For handling media files.
- **openai-whisper**: Whisper model for transcription.

## Installation

1. Clone the repository:

``` bash
   git clone https://github.com/your-username/video-to-text.git
   cd video-to-text
```

1. Set up a virtual environment:

``` bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

1. Install Python dependencies:

``` bash
   pip install -r requirements.txt
```

1. Install **ffmpeg** if not already installed:
    - On Debian/Ubuntu:

``` bash
     sudo apt update && sudo apt install ffmpeg
```

- On macOS (via Homebrew):

``` bash
     brew install ffmpeg
```

- On Windows:
    - Download from [FFmpeg official website](https://ffmpeg.org/download.html).
    - Add `ffmpeg` to your system's PATH.

    1. Ensure `whisper` library from OpenAI is installed:

``` bash
   pip install git+https://github.com/openai/whisper.git
```

## Usage

To process an audio or video file, run the following command in the terminal:

``` bash
python main.py <input_file>
```

### Example:

``` bash
python main.py example.mp4
```

### Output:

- The tool will:
    1. Analyze the input file type (audio or video).
    2. Extract audio if it's a video file.
    3. Transcribe the audio to text.
    4. Save the transcription to a file named `result.txt`.

## Simulated Speaker Diarization Example

Given an input transcription:

``` text
This is the first sentence. This is the second sentence.
```

The processed transcription with speaker simulation:

``` text
Speaker 1: This is the first sentence.
Speaker 2: This is the second sentence.
```

## File Organization

- **main.py**: Entry point for the tool. Handles argument parsing and orchestrates the processing flow.
- **audio_processor.py**: Handles audio extraction from video files using ffmpeg.
- **file_manager.py**: Provides utility functions for file validation and management.
- **transcriber.py**: Uses the Whisper model for audio transcription.
- **speaker_recognition.py**: Simulates speaker diarization for transcribed text.
- **result_saver.py**: Saves the transcription results to a file.

## Potential Improvements

1. Support for real-time speaker diarization.
2. Improved logging and error handling.
3. Support for additional transcription languages and Whisper model sizes as input options.
4. A GUI or web-based interface for easier use.
