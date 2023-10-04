

smiles = [':)', ':D', ';D', ';)']

face = [':-)', ':-D', ';-D', ';-)', ':~)', ':~D', ';~D', ';~)']


def count_smileys(data):
    counter = 0
    for n in data:
        if n in smiles or n in face:
            counter += 1
    return counter


array = [':)', ':D', ';D', ';)']

print(count_smileys(array))