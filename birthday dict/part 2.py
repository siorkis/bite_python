import json

file = open("birthday.json")
birthday = json.load(file)

print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birthday:
    print(key)

name = input("\nWho's birthday do you want to look up?\n")
print(name + "'s birthday is {day}/{month}/{year}".format(day=birthday[name][0],
                                                          month=birthday[name][1],
                                                          year=birthday[name][2]))
file.close()
