countries = ['USA', 'France', 'Japan', 'Brazil', 'Egypt']
capitals = ['Washington D.C.', 'Paris', 'Tokyo', 'Brasilia', 'Cairo']
dictionary = dict(zip(countries, capitals))
print (dictionary['France'])
dictionary.update({'China':'Beijing'})
dictionary.update({'USA':'DC'})
print(f'{list(dictionary.keys())}\n{list(dictionary.values())}')
print('Canada' in dictionary)
del dictionary['Japan']
print(dictionary)
target_country = input()
if target_country in dictionary:
    print(dictionary[target_country])
else:
    print('Country not found')
dictionary_new = {'Canada': 'Ottawa', 'Austria': 'Vienna', 'Chile': 'Santiago'}
dictionary.update(dictionary_new)
print(dictionary)
