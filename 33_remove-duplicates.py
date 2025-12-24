#.set()
my_list=[1,2,3,2,4,3,5]
unique_list=list(set(my_list))
print('updated list:',unique_list)

#for loop()
my_list=[1,2,3,2,4,3,5]
unique_list=[]
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print('Updated list:',unique_list)

#fromkeys()
my_list=[1,2,3,2,4,3,5]
unique_list=list(dict.fromkeys(my_list))
print('updated list:',unique_list)