appointments = []
MAX_MINUTES = 240

def calculate_total_minutes():
    return sum(a["duration"] for a in appointments)

@app.post("/askbot")
async def ask_bot(q: Question):
    user_input = q.question.lower()

    # Booking logic
    if "appointment" in user_input or "book" in user_input:
        duration = 30

        if calculate_total_minutes() + duration > MAX_MINUTES:
            return {"response": "Sorry, no available slots today. Please try another day."}

        appointment = {
            "id": len(appointments) + 1,
            "duration": duration
        }
        appointments.append(appointment)

        return {"response": f"✅ Appointment booked! ID: {appointment['id']}"}

    # AI response
    try:
        response = llm([HumanMessage(content=q.question)])
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}
