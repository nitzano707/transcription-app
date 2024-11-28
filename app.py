from fastapi import FastAPI, File, UploadFile
from faster_whisper import WhisperModel

app = FastAPI()

# טוען את מודל התמלול
model = WhisperModel("ivrit-ai/faster-whisper-v2-d4", device="cpu")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # שמירת קובץ האודיו
    with open(file.filename, "wb") as f:
        f.write(await file.read())

    # תמלול האודיו
    segments, _ = model.transcribe(file.filename, language="he")
    transcription = [{"start": seg.start, "end": seg.end, "text": seg.text} for seg in segments]

    return {"transcription": transcription}
