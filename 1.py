from datetime import date

name, age, repeat = input("Input your name, age, number of repeat in the following format: name age number\n").split()

age = int(age)
repeat = int(repeat)

current_year = date.today().year
born_year = current_year - age

# sub tack 1
print(str(born_year + 100)*repeat, end='\n')

# sub tack 2
for i in range(repeat):
    print(str(born_year + 100), end='\n')
