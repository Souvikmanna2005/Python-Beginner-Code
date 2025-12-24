#list comprehension
my_list=[10,20,30,40,50]
element_to_delete=int(input('Enter the element you want to delete='))
my_list=[x for x in my_list if x!=element_to_delete]
print('updated list:',my_list)

#remove
my_list=[10,20,30,40,50]
element_to_delete=int(input('Enter the element you want to delete='))
for i in my_list:
    if i==element_to_delete:
        my_list.remove(i)
        break
print('Updated list:',my_list)

#del
my_list=[10,20,30,40,50]
element_to_delete=int(input('Enter the element you want to delete='))
if element_to_delete in my_list:
    index=my_list.index(element_to_delete)
    del my_list[index]
    print('Updated list:',my_list)

#filter()
my_list=[10,20,30,40,50]
element_to_delete=int(input('Enter the element you want to delete='))
my_list=list(filter(lambda x: x!=element_to_delete,my_list))
print('updated list:',my_list)
