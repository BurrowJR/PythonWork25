persons_name_country = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
    }

print(persons_name_country['Alice'])
print(persons_name_country['Francois'])
print(persons_name_country['Inti'])
print(persons_name_country['Monika'])
print(persons_name_country['Sanyu'])
print(persons_name_country['Yoshitaka'])
print()
for key, value in persons_name_country.items():
    print(f'{key}: {value}')