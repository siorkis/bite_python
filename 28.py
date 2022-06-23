def maximum(a, b, c):
    if a > b and a > c:
        print(a, "is maximum")
    elif b > a and b > c:
        print(b, "is maximum")
    elif a == b and a == c:
        print("numbers are equal")
    else:
        print(c, "is maximum")

first, second, third = input("Enter the numbers:\n").split()
first = int(first)
second = int(second)
third = int(third)

maximum(first, second, third)
