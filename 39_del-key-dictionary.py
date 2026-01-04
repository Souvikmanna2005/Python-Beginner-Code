data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
keys_to_delete = ['b', 'd']
for key in keys_to_delete:
    if key in data:
        del data[key]

print(data)