#Create a dictionary by extracting the list of key from the given dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
keys_to_extract = ['a', 'c']
extracted_dict = {}
for key in keys_to_extract:
    if key in data:
        extracted_dict[key] = data[key]
print(extracted_dict)

