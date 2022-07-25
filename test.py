from states_as_list import coords

guessed_states = ["Alaska", "California"]

all_states = []
for key in coords:
    all_states.append(key)

print(guessed_states)
print(all_states)

missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

print(missed_states)
