list=[1,2,2,3,3,3,4,4,4,4,7]
element=int(input('Enter the element to count occurrences='))
count=0

for num in list:
    if num==element:
        count += 1
print(f'Element {element} occurs {count} times in the list')