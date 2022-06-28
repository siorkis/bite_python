import json

f = open("birthday.json")
birthday = json.load(f)


months = { 1: "January",
           2: "February",
           3: "March",
           4: "April",
           5: "May",
           6: "June",
           7: "July",
           8: "August",
           9: "September",
           10: "October",
           11: "November",
           12: "December"}

output = {}
counter = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}

for name in birthday:
    month = birthday[name][0]
    counter[month].append(1)
    output[months[month]] = len(counter[month])

# print(output)
for key in output:
    print(key + ":" + str(output[key]))
