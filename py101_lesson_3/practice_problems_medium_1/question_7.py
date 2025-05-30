# One day, Spot was playing with the Munster family's home computer,
# and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

print(munsters)

# Yes the munsters family data is changed. Dictionaries are mutable so the objects
# being referenced in mess_with_demographics(munsters) are mutated to the new value.
# value is a reference to each nested dictionary, not a copy.