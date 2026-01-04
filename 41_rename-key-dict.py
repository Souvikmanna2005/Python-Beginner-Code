data = {'name': 'Souvik', 'age': 22, 'city': 'Midnapore'}

new_key = 'location'
old_key = 'city'

if old_key in data:
    data[new_key] = data[old_key]
    del data[old_key]

print(data)