with open('numbers1.txt') as o:
    numbers_one = [line[:-1] for line in o]

with open('numbers2.txt') as t:
    numbers_two = [line[:-1] for line in t]

result = []

for number in numbers_one:
    if number in numbers_two:
        result.append(number)

print(result)
