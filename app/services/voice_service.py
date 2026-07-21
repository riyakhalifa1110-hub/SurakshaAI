import whisper
import tempfile
import os

# Load model only once
model = whisper.load_model("base")


def speech_to_text(audio_file):
    """
    Convert uploaded audio to text using Whisper.
    """

    suffix = os.path.splitext(audio_file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        audio_file.save(temp.name)
        temp_path = temp.name

    result = model.transcribe(temp_path)

    os.remove(temp_path)

    return result["text"]