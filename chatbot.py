import random

def chatbot():
    print("Hello! I'm your friendly chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["exit", "bye", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            greetings = ["Hello!", "Hi there!", "Hey! How's it going?"]
            print(f"Chatbot: {random.choice(greetings)} How can I assist you today?")
        
        # Asking for the chatbot's name
        elif "your name" in user_input:
            print("Chatbot: I'm a simple yet clever chatbot here to assist you with basic queries.")
        
        # Asking for help
        elif "help" in user_input:
            print("Chatbot: Sure, I'm here to help! What do you need assistance with?")
        
        # Asking about the weather
        elif "weather" in user_input:
            print("Chatbot: I can't provide real-time weather updates, but it's always a good idea to check a reliable weather service!")
        
        # Asking about the user's mood
        elif "how are you" in user_input:
            responses = ["I'm just a program, but I'm doing great! How about you?", "I'm here to help you, so I'm always good!"]
            print(f"Chatbot: {random.choice(responses)}")
        
        # Small talk: asking the user how they are
        elif "i'm good" in user_input or "i'm fine" in user_input:
            print("Chatbot: I'm glad to hear that! Is there anything specific you'd like to talk about?")

        # Random advice
        elif "advice" in user_input:
            advice_list = [
                "Always be yourself; everyone else is already taken.",
                "Believe in yourself and all that you are.",
                "Strive not to be a success, but rather to be of value."
            ]
            print(f"Chatbot: Here's some advice: {random.choice(advice_list)}")
        
        # Default response
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()
