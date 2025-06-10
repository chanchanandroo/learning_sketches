#print("straight quotes test")

#moods = ["angry", "sad", "happy", "calm", "anxious"]

#happy_and_calm_vibes_only = list(filter(lambda x: "happy", "calm", moods))

#print(happy_and_calm_vibes_only)

#corrected version:

moods = ["angry", "sad", "happy", "calm", "anxious"]

happy_and_calm_vibes_only = list(filter(lambda x: x in ["happy", "calm"], moods))

print(happy_and_calm_vibes_only)
