def greetings(name, work):
    full_name = " ".join(name)
    title = work["title"]
    occupation = work["occupation"]
    return f"Hello, {full_name}! Nice to have a {title} {occupation} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.  
