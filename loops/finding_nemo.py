# Loop over the elements of the 'fish_list' below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for name in fish_list:
    print(name)
    if name == 'Nemo':
        break

print()
# or use a while loop

index = 0

while index < len(fish_list):
    print(fish_list[index])
    if fish_list[index] == 'Nemo':
        break

    index += 1
