from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "NIZAR AI",
        "status": "ONLINE",
        "message": "Salam Nizar! Ana assistant dyalk."
    }
