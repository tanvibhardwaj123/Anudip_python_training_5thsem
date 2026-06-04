#Accept a number from the user and determine whether it is a prime number or not and print its factors.
num = int(input("Enter a number: "))

i = 1
count = 0

print("Factors:", end=" ")

while i <= num:
    if num % i == 0:
        print(i, end=" ")
        count += 1
    i += 1

print()

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
