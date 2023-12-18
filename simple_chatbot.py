# Define some predefined responses
responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thank you!",
    "bye": "Goodbye!",
    # Add more responses as needed
}

# Function to get the bot's response
def get_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm not sure how to respond to that."

# Main function to run the chatbot
def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
