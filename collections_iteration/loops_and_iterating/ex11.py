my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

outer_index = 0

while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        element = my_list[outer_index][inner_index]
        if element % 2 == 0:
            print(element)
        inner_index += 1
    outer_index += 1

print()

def even_elements(my_list, outer_index=0, inner_index=0):
    if outer_index >= len(my_list):
        return
    if inner_index < len(my_list[outer_index]):
        element = my_list[outer_index][inner_index]
        if element % 2 == 0:
            print(element)
        even_elements(my_list, outer_index, inner_index + 1)
    else:
        even_elements(my_list, outer_index +1, 0)

even_elements(my_list)