# The following function unnecessarily uses two return statements
# to return boolean values. Can you rewrite this function so it only
# has one return statement and does not explicitly use either
# True or False?

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False

# conditional expression
# def is_color_valid(color):
#     return color == "blue" or color == "green"

# in operator
def is_color_valid(color):
    return color in {"blue", "green"}


print(is_color_valid("blue"))
print(is_color_valid("green"))
print(is_color_valid("pink"))
