# Write a Python program that takes an integer as input and checks if the number is prime.
num = int(input("Enter an integer: "))
count = 0

for i in range(2,int(num ** 0.5)+ 1):
    if num % i == 0:
        count = count + 1
if count == 1:
    print(count)
    print("It is a prime number")
else:
    print(count)
    print("It is not Prime Number")
