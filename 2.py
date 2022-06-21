number, check = input("Input a number and check:\n").split()
number = int(number)
check = int(check)

# main task
# if (number % 2) == 0:
#     if (number % 4) == 0:
#         print("Number is multiple of 4")
#     print('Number is even')
# else:
#     print("Number is odd")

if (number % check) == 0:
    print("{} is multiple of {}".format(number, check))
else:
    print("{} is not multiple of {}".format(number, check))
