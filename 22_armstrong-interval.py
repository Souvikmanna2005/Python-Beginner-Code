lower=int(input('Enter lower range:'))
upper=int(input('Enter upper range:'))
print(f'Armstrong number between {lower} and {upper} are:')
for num in range(lower,upper+1):
    n=len(str(num))
    sum_of_powers=sum(int(digit)**n for digit in str(num))
    if num==sum_of_powers:
        print(num)