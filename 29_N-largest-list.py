numbers=[10,5,8,20,3,15]
n=int(input('Enter how many largest number i want:'))
largest_numbers=sorted(numbers,reverse=True)[:n]
print(f'{n} largest number in a list:',largest_numbers)