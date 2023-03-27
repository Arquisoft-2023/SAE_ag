from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
import os

from tutorias.Index import tutorias

load_dotenv()
app = FastAPI()

app.include_router(tutorias, prefix="/tutorias")

#Development -> reload = True
if __name__ == "__main__":
    import uvicorn
    URI = str(os.environ.get("URI"))
    PORT = int(os.environ.get("PORT"))
    uvicorn.run(f"{Path(__file__).stem}:app", host=URI, port=PORT, reload=True)