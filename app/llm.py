def generate_ai_response(prompt):
    print("⚡ DEMO MODE ACTIVE")

    if "Sales" in prompt:
        return """• Lead is warm but disengaged  
• Requires timely follow-up  
• Risk of losing interest if delayed"""

    elif "Action" in prompt:
        return """• Send follow-up email  
• Call within 24 hours  
• Share additional value (case study)"""

    elif "Execution" in prompt:
        return """Morning: Follow-up emails  
Afternoon: Client calls  
Evening: Review pipeline"""

    else:
        return "AI response"
