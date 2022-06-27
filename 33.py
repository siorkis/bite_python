birthday = {"Albert Einstein": [3, 14, 1879],
            "Benjamin Franklin": [1, 17, 1706],
            "Ada Lovelace": [12, 10, 1815]
            }

print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birthday:
    print(key)

name = input("\nWho's birthday do you want to look up?\n")
print(name + "'s birthday is {day}/{month}/{year}".format(day=birthday[name][0],
                                                          month=birthday[name][1],
                                                          year=birthday[name][2]))
