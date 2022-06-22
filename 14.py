def first(list_one):
    list_one = list(set(list_one))
    print(list_one)

def second(list_one, list_two):
    for elem in list_one:
        if elem not in list_two:
            list_two.append(elem)
    print(list_two)

array = [2, 2, 3, 3, 4, 5, "apple", "apple", "red"]
array_2 = [2, 2, 3, 3, 4, 5, "apple", "apple", "red"]
array_3 = []
first(array)
second(array_2, array_3)
