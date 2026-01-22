from collections import defaultdict
from datetime import datetime

# In-memory metrics store
metrics = defaultdict(int)

# Track last activity time
last_activity = {
    "timestamp": None
}

def increment(metric_name: str):
    metrics[metric_name] += 1
    last_activity["timestamp"] = datetime.utcnow().isoformat()

def get_metrics():
    return {
        "metrics": dict(metrics),
        "last_activity": last_activity["timestamp"]
    }
