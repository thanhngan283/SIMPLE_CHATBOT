def get_response(message: str) -> str:
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"
    elif "name" in message:
        return "I am a simple chatbot."
    elif "time" in message:
        return "I cannot tell time yet, but I am learning!"
    elif "bye" in message:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that."
