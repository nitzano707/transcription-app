from fastapi import FastAPI, File, UploadFile
from faster_whisper import WhisperModel

app = FastAPI()

model = WhisperModel("ivrit-ai/faster-whisper-v2-d4", device="cuda")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        f.write(await file.read())

    segments, _ = model.transcribe(file.filename, language="he")
    transcription = [{"start": seg.start, "end": seg.end, "text": seg.text} for seg in segments]

    return {"transcription": transcription}
