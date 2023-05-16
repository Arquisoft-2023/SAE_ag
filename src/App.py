from dotenv import load_dotenv
from fastapi import FastAPI
from pathlib import Path
from starlette.middleware.cors import CORSMiddleware
import os

from gestionUsuarios.Index import gestionUsuarios
from autenticacion.Index import autenticacion
from formularios.Index import formularios
from remisiones.Index import remisiones
from tutorias.Index import tutorias
from starlette.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

# Configuracion provicional de CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gestionUsuarios, prefix="/gestionUsuarios")
app.include_router(formularios, prefix="/formularios")
app.include_router(remisiones, prefix="/remisiones")
app.include_router(autenticacion, prefix="/auth")
app.include_router(tutorias, prefix="/tutorias")



#Development -> reload = True
if __name__ == "__main__":
    import uvicorn
    URI = str(os.environ.get("URI"))
    PORT = int(os.environ.get("PORT"))
    uvicorn.run(f"{Path(__file__).stem}:app", host=URI, port=PORT, reload=True)