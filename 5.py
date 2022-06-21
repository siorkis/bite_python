import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
common_two = []

if len(b) > len(a):
    a, b = b, a

for number in a:
    if number in b and number not in common:
        common.append(number)

print(common)

list_one = []
list_two = []

for i in range(2):
    times = random.randint(1, 15)
    for j in range(times):
        number = random.randint(1, 100)
        if i == 0:
            list_one.append(number)
        list_two.append(number)

if len(list_two) > len(list_one):
    list_one, list_two = list_two, list_one

for number in list_one:
    if number in list_two and number not in common_two:
        common_two.append(number)

# print(list_one)
# print(list_two)
print(common_two)
