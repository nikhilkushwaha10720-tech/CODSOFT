import datetime
import random
import os

# SmartBot with Name Memory

MEMORY_FILE = "user_memory.txt"

# Load saved name
def load_name():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return file.read().strip()
    return ""

# Save name
def save_name(name):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        file.write(name)

# User memory
user_name = load_name()

print("=" * 50)
print("          Welcome to SmartBot")
print("=" * 50)
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        print("Bot: Please enter a message.")
        continue

    # Lowercase version for matching
    msg = user_input.lower()

    # Goodbye
    if msg in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    # Greetings
    elif any(word in msg for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to meet you!"
        ]
        print("Bot:", random.choice(greetings))

    # Save user's name
    elif msg.startswith("my name is"):
        name = user_input[10:].strip()

        if name:
            user_name = name
            save_name(user_name)
            print(f"Bot: Nice to meet you, {user_name.title()}!")
        else:
            print("Bot: Please tell me your name after 'My name is'.")

    # Recall user's name
    elif msg in ["what is my name", "who am i", "tell me my name"]:
        if user_name:
            print(f"Bot: Your name is {user_name.title()}.")
        else:
            print("Bot: I don't know your name yet. Tell me using 'My name is ...'")

    # Bot name
    elif "your name" in msg:
        print("Bot: My name is SmartBot.")

    # How are you
    elif "how are you" in msg:
        responses = [
            "I'm doing great. Thanks for asking!",
            "I'm fine and ready to help you.",
            "All good! How about you?"
        ]
        print("Bot:", random.choice(responses))

    # Time
    elif "time" in msg:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

    # Date
    elif "date" in msg:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    # Day
    elif "day" in msg:
        current_day = datetime.datetime.now().strftime("%A")
        print(f"Bot: Today is {current_day}")

    # Help
    elif "help" in msg:
        print("""
Bot: I can help you with:

• Greetings
• Remembering your name
• Date and Time
• Day Information
• Basic Conversation
• Jokes
• Customer Support
• Exit Command
        """)

    # Joke
    elif "joke" in msg:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer get cold? It forgot to close its Windows!",
            "Why do Java developers wear glasses? Because they don't C#.",
            "There are only 10 types of people: those who understand binary and those who don't."
        ]
        print("Bot:", random.choice(jokes))

    # Support
    elif "support" in msg or "contact" in msg:
        print("Bot: Please contact customer support at support@example.com")

    # Weather
    elif "weather" in msg:
        print("Bot: Sorry, I cannot access live weather information.")

    # Thank you
    elif "thank" in msg:
        print("Bot: You're welcome!")

    # Age
    elif "your age" in msg:
        print("Bot: I don't have an age. I am a computer program.")

    # Creator
    elif "who created you" in msg:
        print("Bot: I was created by a Python developer named Nikhil Kumar Kushwaha.")

    # Can you...
    elif msg.startswith("can you"):
        print("Bot: I'll try my best to help you with that.")

    # Math operations
    elif msg.startswith("calculate"):
        try:
            expression = user_input[9:].strip()
            result = eval(expression)
            print(f"Bot: The answer is {result}")
        except:
            print("Bot: Invalid mathematical expression.")

    # Unknown input
    else:
        unknown_responses = [
            "Sorry, I didn't understand that.",
            "Could you rephrase your question?",
            "I'm not sure what you mean.",
            "Please try asking in a different way."
        ]
        print("Bot:", random.choice(unknown_responses))