def get_response(user_input):
    if "hi" in user_input.lower():
        return "Hi there! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but thanks for asking!"
    elif "can you help me to solve the questions" in user_input.lower():
        return "Sure, what do you need help with?"
    elif "what can you do" in user_input.lower():
        return "I can answer your questions and engage in simple conversations."
    elif "what is the largest prime number less than hundred" in user_input.lower():
        return "The largest prime number less than 100 is 97."
    elif "how do chatbots work" in user_input.lower():
        return "Chatbots work by processing user input, analyzing it using algorithms, and generating appropriate responses based on predefined rules or machine learning models."
    elif "what are some common applications of chatbots" in user_input.lower():
        return "Chatbots are used in various applications, including customer service, sales and marketing, virtual assistants, healthcare, and e-commerce."
    elif "how do chatbots improve customer experience?" in user_input.lower():
        return "Chatbots improve customer experience by providing instant responses, 24/7 availability, personalized interactions, and seamless integration across multiple channels."
    elif "what are the limitations of chatbots?" in user_input.lower():
        return "Some limitations of chatbots include their inability to understand complex or ambiguous queries, limitations in handling nuanced conversations."
    elif "goodbye" in user_input.lower():
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting with me. Type 'goodbye' to exit.")

    while True:
        user_input = input("You: ").strip()  # Remove leading/trailing whitespace
        if user_input.lower() == 'goodbye':  # Simplify exit condition
            print("ChatBot: Goodbye! Have a nice day!")
            break
        elif user_input:  # Check if input is not empty
            response = get_response(user_input)
            print("ChatBot:", response)
        else:
            print("ChatBot: Please say something.")

if __name__ == "__main__":
    main()
