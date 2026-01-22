import re

def analyze_command(command: str) -> dict:
    text = command.lower().strip()

    # ALERTS FIRST (highest priority)
    if re.search(r"(alert|notify|warning)", text):
        return {
            "intent": "send_alert",
            "priority": "medium",
            "action": "notify"
        }

    # SYSTEM CHECKS SECOND
    if re.search(r"(check|status|health|monitor)", text):
        return {
            "intent": "system_check",
            "priority": "high",
            "action": "run_monitor"
        }

    # DEFAULT FALLBACK
    return {
        "intent": "unknown",
        "priority": "low",
        "action": "log_only"
    }
