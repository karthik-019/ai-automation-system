from app.services.email_service import send_email_alert

def execute_action(action: str) -> str:
    print(f"⚙️ execute_action called with action = {action}")

    if action == "run_monitor":
        print("🩺 Running system monitor")
        return "System monitoring task executed"

    if action == "notify":
        print("🚨 Triggering email alert")
        send_email_alert(
            subject="AI Automation Alert",
            body="An alert condition was triggered by the automation system."
        )
        return "Alert email sent"

    print("📝 Logging only")
    return "Action logged only"
