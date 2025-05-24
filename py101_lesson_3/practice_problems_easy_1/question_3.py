famous_words = "seven years ago..."
# string concatenation
new_string = "Four score and " + famous_words
print(new_string)

more_famous_words = "Four score and "
# using join()
new_string_2 = "".join([more_famous_words, famous_words])
print(new_string_2)
# using format()
new_string_3 = "{} {}".format(more_famous_words, famous_words)
print(new_string_3)
# using string interpolation
new_string_4 = f"{more_famous_words} {famous_words}"
print(new_string_4)
