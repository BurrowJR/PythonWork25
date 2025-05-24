def print_in_box(string, max_width=None):
    if max_width and max_width > 4:
        if len(string) > max_width - 2:
            string = string[:max_width - 3] + "..."
        else:
            string

    width = len(string) + 2
    border = "+" + "-" * width + "+"
    space = "|" + " " * width + "|"

    print(border)
    print(space)
    print(f"| {string} |")
    print(space)
    print(border)

print_in_box("Hello World!")
print_in_box("")
print_in_box("This is a very long string and will be cut" \
" off because we give a truncated width.", 20)
print_in_box("This string will be printed because no truncated width is given.")

print()
from textwrap import wrap

def print_in_box_2(string, max_width=None):
    if max_width and max_width > 4:
        wrapped_string = wrap(string, max_width - 2)
    else:
        wrapped_string = [string]
        
    width = max_width if max_width else len(string) + 2
    border = "+" + "-" * width + "+"
    space = "|" + " " * width + "|"

    print(border)
    print(space)
    for string in wrapped_string:
        print(f"| {string.ljust(width - 2)} |")
    print(space)
    print(border)

print_in_box_2("Hello World!")
print_in_box_2("")
print_in_box_2("This is a very long string but it will not be cut" \
" off because we use word wrap here.", 20)
print_in_box_2("This string will be printed on one line because no truncated width is given.")
print_in_box_2("I like word wrap better than cutting off" \
" my string.", 20)
