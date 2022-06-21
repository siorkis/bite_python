a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_a = []

# a.sort(key= lambda i : i % 2)

def even(a):
    if a % 2 == 0:
        return True

a = filter(even, a)

for i in a:
    new_a.append(i)

print(new_a)
