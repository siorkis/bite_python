import matplotlib.pyplot as plt
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

ox = []
oy = []

for key in output:
	ox.append(key)
	oy.append(output[key])


plt.plot(ox, oy)

plt.ylabel('Number')
plt.xlabel('Month')
plt.show()

