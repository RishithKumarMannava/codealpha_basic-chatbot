def chatbot_reply(message):
    message = message.lower()

    if message == "hello":
        return "Hi there! 👋"
    elif message == "how are you":
        return "I'm just a bunch of code, but I'm doing great!"
    elif message == "what's your name":
        return "I'm your friendly chatbot 🤖"
    elif message == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Hmm, I didn't understand that."

# Start chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_reply(user_input)
    print("Chatbot:", response)

    if user_input.lower() == "bye":
        break