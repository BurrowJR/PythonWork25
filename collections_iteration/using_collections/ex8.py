# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text)
text_section = (text[21:35])
print(text[21:35].rfind('f'))
print(f'''
      text[21:35] is slicing text and returning "{text_section}".
      Then the .rfind method looks for the rightmost index of "f" within the substring, which is at index 8.
      ''')

print(text.rfind('f', 21, 35))
print(f'''
      The .rfind method is looking for the rightmost index of "f" between the indexes 21:35, so it start looking at index 21 and stops at 35 returning index 29. 
      ''')