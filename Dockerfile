# בסיס ל-Docker Image עם GPU
FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

# התקנת Python וכלים נדרשים
RUN apt-get update && apt-get install -y python3 python3-pip

# התקנת הספריות הדרושות
RUN pip install faster-whisper fastapi uvicorn

# יצירת תיקיית עבודה
WORKDIR /app

# העתקת הקבצים למיכל
COPY . /app

# הורדת מודל התמלול מראש
RUN python3 -c "from faster_whisper import WhisperModel; \
    WhisperModel('ivrit-ai/faster-whisper-v2-d4', device='cpu')"

# הפעלת האפליקציה
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
