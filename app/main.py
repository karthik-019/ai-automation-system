from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Automation Control System",
    description="AI-powered automation & monitoring system",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "running"}
