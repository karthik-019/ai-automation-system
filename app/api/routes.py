from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai import analyze_command
from app.services.automation import execute_action
from app.services.metrics import increment, get_metrics
from app.services.logger import log_event

router = APIRouter()


# ---------------- Request Model ----------------

class CommandRequest(BaseModel):
    command: str


# ---------------- Core Command Endpoint ----------------

@router.post("/command")
def handle_command(request: CommandRequest):
    # 🔹 Track total API requests
    increment("total_requests")

    # 🔹 AI decision
    intent = analyze_command(request.command)

    # 🔹 Execute automation action
    result = execute_action(intent["action"])

    # 🔹 Track action type
    increment(f"action_{intent['action']}")

    # 🔹 Structured logging
    log_event(
        event_type="command_processed",
        data={
            "command": request.command,
            "intent": intent,
            "result": result
        }
    )

    return {
        "intent": intent,
        "result": result
    }


# ---------------- Metrics Endpoint ----------------

@router.get("/metrics")
def metrics():
    return get_metrics()
