with open('data.txt') as f:
    lines = f.readlines()

array = []
categories = {}

for line in lines:
    try:
        if line.split("/")[2][-1] != '\n':
            array.append(line.split("/")[2])
    except:
        pass

for category in array:
    categories[category] = array.count(category)

print(categories)
