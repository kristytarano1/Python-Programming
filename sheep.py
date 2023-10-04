array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]

def count_sheeps(sheep):
    counter = 0
    for n in sheep:
        if n == True:
            counter += 1
        else:
            pass
    return counter
    
print(count_sheeps(array1))