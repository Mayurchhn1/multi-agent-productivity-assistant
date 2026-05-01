# -----------------------------
# 🎯 INTENT DETECTION AGENT
# -----------------------------

def detect_intent(user_input: str) -> str:
    text = (user_input or "").lower()

    # 🔥 Sales intent
    if any(word in text for word in [
        "sale", "sales", "client", "deal", "revenue",
        "pipeline", "lead", "closing"
    ]):
        return "sales"

    # 📚 Learning intent
    if any(word in text for word in [
        "learn", "study", "course", "skill", "training"
    ]):
        return "learning"

    # 💼 Work intent
    if any(word in text for word in [
        "work", "task", "project", "todo", "organize"
    ]):
        return "work"

    # 🧠 Default
    return "general"
