a = [5, 10, 15, 20, 25]
new_a = []

def new_list(array_initial, array_new):
    for i in range(-1, 1):
        array_new.append(array_initial[i])
    return array_new

new_list(a, new_a)
print(new_a)
