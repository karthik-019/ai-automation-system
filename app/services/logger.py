from datetime import datetime

def log_event(event_type: str, data: dict):
    timestamp = datetime.utcnow().isoformat()

    log_entry = {
        "timestamp": timestamp,
        "event_type": event_type,
        "data": data
    }

    print(f"📝 LOG → {log_entry}")
