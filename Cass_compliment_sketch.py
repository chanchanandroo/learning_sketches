compliments = ['You\'re doing great', 'Keep going', 'I\'m proud of you']

expected_output = list(map(lambda x: x.print(), compliments))

print(f"Cass: {expected_output}")

#corrected version:

compliments = ["You're doing great", "Keep going", "I'm proud of you"]

expected_output = list(map(lambda x: f"💛 Cass: {x}", compliments))

for line in expected_output:
    print(line)