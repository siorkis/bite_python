number = int(input("Enter a number\n"))
divisors = []

for i in range(1, number+1):
    if number % i == 0:
        divisors.append(i)

if len(divisors) == 2 and divisors[1] == number:
   print("Number is prime")
else:
    print("Number is not prime")
