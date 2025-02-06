class SpeakerRecognition:
    """Simulate speaker diarization for a transcription."""

    @staticmethod
    def process_transcription(transcription: str) -> str:
        # Simulated speaker diarization: alternate between Speaker 1 and Speaker 2.
        lines = transcription.split(". ")
        processed_lines = []
        for i, line in enumerate(lines):
            speaker = f"Speaker {i % 2 + 1}"
            processed_lines.append(f"{speaker}: {line.strip()}")
        return "\n".join(processed_lines)
