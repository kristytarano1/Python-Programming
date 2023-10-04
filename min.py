array1 =[1, 2, 3, 4, 5, 1]


def remove_smallest(n):
    if n == []:
        return n
    else:
        z = list(n)
        mini = min(z)
        z.remove(mini)
        return z
    

print(remove_smallest(array1))

