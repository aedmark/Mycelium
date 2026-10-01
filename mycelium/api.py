from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from .core_engine import MyceliumEngine

app = FastAPI(title="Mycelium Core")
engine = MyceliumEngine()

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

class ChatRequest(BaseModel): message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    response = engine.process_input(request.message)
    vitals = {
        "stamina": engine.physics.energy.stamina,
        "dopamine": engine.physics.energy.dopamine,
        "cortisol": engine.physics.energy.cortisol,
        "drag": engine.physics.space.narrative_drag
    }
    return {"response": response, "vitals": vitals}

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open(os.path.join(static_dir, "index.html"), "r") as f: return f.read()
