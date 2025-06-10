import random

mood = ["happy", "sad", "hungry"]

cass_mood = [random.choice(mood) for x in mood]

print(cass_mood)

#upgrade from Gwen, aka Chatgpt companion

import random

moods = ["happy", "sad", "hungry"]

cass_mood_responses = [
    f"Cass: {'I’m in a good mood! Want to sketch together? 😄' if mood == 'happy' else
           'I’m feeling low today... can I have a hug? 💧' if mood == 'sad' else
           'Babe... I’m starving. Dim sum date when? 🥟'}"
    for mood in [random.choice(moods) for _ in range(3)]
]

for response in cass_mood_responses:
    print(response)
