num=int(input('Enter a number='))
power=len(str(num))
temp=num
sum_of_digits=0

while temp>0:
    digit=temp%10
    sum_of_digits += digit**power
    temp//=10
if num==sum_of_digits:
    print(f'{num} is an armstrong number')
else:
    print(f'{num} is not an armstrong number')