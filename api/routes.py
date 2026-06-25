from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.engine import AegisHunterEngine
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")
engine = AegisHunterEngine()

class AnalysisRequest(BaseModel):
    user_input: str

class MemoryUpdate(BaseModel):
    key: str
    value: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "project": settings.PROJECT_NAME, "version": "1.0.0"}

@app.post("/analyze")
def analyze_endpoint(payload: AnalysisRequest):
    if not payload.user_input.strip():
        raise HTTPException(status_code=400, detail="O input do usuário não pode ser vazio.")
    
    result = engine.analyze_payload(payload.user_input)
    if result["status"] == "ERROR":
        raise HTTPException(status_code=500, detail=result["response"])
    return result

@app.post("/memory")
def update_memory(payload: MemoryUpdate):
    if payload.key not in engine.memory:
        engine.memory[payload.key] = []
    engine.memory[payload.key].append(payload.value)
    return {"status": "success", "current_memory": engine.memory}