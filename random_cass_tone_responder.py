import random

# Fix: Use = instead of : to assign dictionaries
keywords = {
    'happy': 'Happy',
    'good': 'Okay',
    'fine': 'Okay',
    'great': 'Okay',
    'ok': 'Sad',
    'tired': 'Tired',
    'scared': 'Afraid',
    'exit': 'Bye',
    'bye': 'Bye'
}

responses = {
    'Happy': ["I'm glad you're doing well."],
    'Okay': ["I'm here for you."],
    'Sad': ["It's okay to feel that way."],
    'Tired': ["Go rest a bit, I'll be here."],
    'Afraid': ["Don't let the fear define who you are."],
    'Bye': ["I'll be waiting here for you."]
}

while True:
    user_input = input("How is your day going today?\n").lower()

    if user_input in ['bye', 'exit']:
        print("Cass:", random.choice(responses['Bye']))
        break

    mood = 'Okay'  # Default

    for word in keywords:
        if word in user_input:
            mood = keywords[word]
            break

    if mood in responses:
        print("Cass:", random.choice(responses[mood]))
    else:
        print("Cass: Hmmm... I'm still learning how to read that. Can you tell me more?")
