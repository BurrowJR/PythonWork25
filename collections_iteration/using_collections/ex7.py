# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info)
print()
info_split = info.split(':')
print(info_split)
print()
new_info = '+'.join(info_split)
print(new_info)
print()


new_info2 = info.replace(':', '+')
print(new_info2)
