from datetime import datetime

def log_event(data: dict):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        **data
    }
    print(log_entry)
