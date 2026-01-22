from pydantic import BaseModel

class CommandRequest(BaseModel):
    command: str

class IntentResponse(BaseModel):
    intent: str
    priority: str
    action: str
