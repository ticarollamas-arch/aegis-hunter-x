import os
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "Aegis Hunter-X"
    API_PORT: int = int(os.getenv("PORT", 8080))
    LLM_API_URL: str = os.getenv("LLM_API_URL", "http://localhost:11434/api/generate")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "llama3")
    SECURITY_THRESHOLD: int = 75

settings = Settings()