order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 14, 15, 16, 17, 18, 19, 20]

number = int(input("Enter the number:\n"))


def simple_check(array, num):
    if num in array:
        print(True)
    else:
        print(False)


def binary_check(array, num):
    length = len(array)
    index = length // 2

    while True:
        if array[index] == num:
            print(True)
            break
        elif array[index] == array[0] or array[index] == array[-1]:
            print(False)
            break
        elif array[index] > num:
            index //= 2
        elif array[index] < num:
            index = (length - index) // 2 + index


simple_check(order, number)
binary_check(order, number)
