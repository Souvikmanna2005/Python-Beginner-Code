my_dict = {'a':6, 'b':8, 'c':3 }
# Sorting dictionary in ascending order
ascending=dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary in ascending order:", ascending)

# Sorting dictionary in descending order
descending=dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))    
print("Dictionary in descending order:", descending)