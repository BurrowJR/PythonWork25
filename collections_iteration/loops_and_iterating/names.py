names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)

# for loop
names2 = ['Fred', 'George', 'Ron', 'Hermione']
upper_names2 = []

for name in names2:
    #if name == 'Ron':
     #   continue
    #upper_name2 = name.upper()
    #upper_names2.append(upper_name2)
    #  same as
    
    if name != 'Ron':
        upper_name2 = name.upper()
        upper_names2.append(upper_name2)

print(upper_names2)
