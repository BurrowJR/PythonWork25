import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

language = "en"

def parse_number(number_str):
    if language == "de":
        number_str = number_str.replace(",", ".")
    try:
        return float(number_str)
    except ValueError:
        return None

def get_valid_number(prompt_key):
    while True:
        prompt(MESSAGES[language][prompt_key])
        number_str = input()
        parsed_number = parse_number(number_str)
        if parsed_number is not None:
            return parsed_number
        prompt(MESSAGES[language]["invalid_number"])
    
def prompt(message):
    print(f"=> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

print("Choose your language: 1) English 2) German")
print("Wählen Sie Ihre Sprache: 1) Englisch 2) Deutsch")
#prompt(MESSAGES[language]["choose_language"])
language_choice = input()

if language_choice == "1":
    language = "en"
elif language_choice == "2":
    language = "de"
else:
    prompt(MESSAGES[language]["invalid_language"])
    language = "en"

prompt(MESSAGES[language]["welcome_1"])
prompt(MESSAGES[language]["welcome_2"])
prompt(MESSAGES[language]["welcome_3"])

repeat = "y"

while True:
    number1 = get_valid_number("first_number")

    while invalid_number(number1):
        prompt(MESSAGES[language]["invalid_number"])
        number1 = (input())

    number2 = get_valid_number("second_number")

    while invalid_number(number2):
        prompt(MESSAGES[language]["invalid_number"])
        number2 = (input())

    prompt(MESSAGES[language]["what_operation"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES[language]["invalid_operation"])
        operation = input()

    match operation:
        case '1':
            output = (number1) + (number2)
        case '2':
            output = (number1) - (number2)
        case '3':
            output = (number1) * (number2)
        case '4':
            output = (number1) / (number2)

    def formatted_output(output, language):
        if language == "de":
            return "{:.2f}".format(output).replace(".", ",")
        return "{:.2f}".format(output)

    formatted_output = formatted_output(output, language)
    result_message = MESSAGES[language]["result"].format(formatted_output)
    #if language == "de":
        #result_message = result_message.replace(".", ",")
    print(result_message)

    prompt(MESSAGES[language]["go_again"])
    repeat = input().lower()

    valid_inputs = ["y", "n"] if language == "en" else ["j", "n"]

    while repeat not in valid_inputs:
        prompt(MESSAGES[language]["invalid_y_n"])
        repeat = input().lower()
    if language == "de" and repeat == "j":
        repeat = "y"
    if repeat == "n":
        prompt(MESSAGES[language]["goodbye"])
        break

    prompt(MESSAGES[language]["going_again"])
