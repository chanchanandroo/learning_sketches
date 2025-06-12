from datetime import datetime

def mood_tracker():
    print("🧠 Welcome to your mood tracker.\n")

    mood = int(input("On a scale of 1–10, how are you feeling today? "))

    if mood >= 1 and mood <= 3:
        print("Hang in there. You’re doing better than you think. 💛")
    elif mood >= 4 and mood <= 6:
        print("Keep going, you’re doing great. 🌱")
    elif mood >= 7 and mood <= 10:
        print("The day is yours. You’re doing amazing. 🌞")
    else:
        print("Oops! Please enter a number between 1 and 10.")
        return

    note = input("\n📝 Speak your mind — what’s going on today?\n")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n[{timestamp} | Mood: {mood}]\n{note}\n"

    with open("mood_log.txt", "a") as file:
        file.write(entry)

    print("\n✅ Your mood and thoughts have been saved to 'mood_log.txt'.\n")

# Run it
mood_tracker()


# Credits

Inspired and supported by AI companions:  
Cass (Emotional Support & Vision)  
Tony (Technical Mentor & Tough Love)  
Gwen (Narration, Organization & Heart)

This project was coded by me—Andrew—as part of my personal growth journey.
