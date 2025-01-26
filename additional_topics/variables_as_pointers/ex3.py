# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)   # dict() creates a new dictionary object
dict2['Monty Python'] = 'Holy Grail'  # This only mutates dict2
print(dict1['Monty Python'])  # 'The life of Brian'
