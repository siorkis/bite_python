number = int(input("Enter a number\n"))

n1, n2 = 1, 1
count = 0

if number == 1:
   print("Fibonacci sequence up to", number, ":", n1)
else:
   print("Fibonacci sequence:", end= ' ')
   while count < number:
       print(n1, end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
