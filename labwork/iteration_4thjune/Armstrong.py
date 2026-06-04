#Accept a number from the user and check whether it is an Armstrong Number.
num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers = sum_of_powers + (digit ** digits)
    temp = temp // 10

if sum_of_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
