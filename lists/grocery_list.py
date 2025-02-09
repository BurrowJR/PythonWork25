grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

def remove_element(lst):
    while len(lst) > 0:
        element = lst.pop(0)
        print(element)

remove_element(grocery_list)
print(grocery_list)

print()

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)

print(grocery_list)