import json

def write_json(new_data, filename='birthday.json'):
    list_obj = []
    with open(filename) as fp:
        list_obj = json.load(fp)
    list_obj.update(new_data)
    with open(filename, 'w') as json_file:
        json.dump(list_obj, json_file,
                  indent=4,
                  separators=(',', ': '))


f = open("birthday.json")
birthday = json.load(f)

print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birthday:
    print(key)

name = input("\nWho's birthday do you want to look up?\n")

print(name + "'s birthday is {day}/{month}/{year}".format(day=birthday[name][0],
                                                          month=birthday[name][1],
                                                          year=birthday[name][2]))
choice = input("\nDo you want to add a person?\n")

if choice == 'yes':
    new_name = input("Enter the name:\n")
    day = int(input('Enter the day:\n'))
    month = int(input("Enter the month\n"))
    year = int(input("Enter the year\n"))
    new_value = {new_name: [day, month, year]}
    write_json(new_value)

f.close()
