a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
order_list = []

for number in a:
    if number >= 5:
        order_list.append(number)

print(order_list)

check = int(input("Enter a number\n"))
order_list = []

for number in a:
    if number < check:
        order_list.append(number)

print(order_list)
