import ast
from collections import Counter


# Function for reading wanted file
def read_File(file):

    with open(file, 'r') as f:
        lines = f.read()
    f.close()
    return lines.splitlines()


# For the example, the file 'dictionaries.txt' was created
lines_list = read_File('dictionaries.txt')
keys = []
dict_list = []
counter = 0
for x in lines_list:
    dictionary = ast.literal_eval(x)  # Create a new dictionary from the data

    # Incrementing a list with all the keys
    if counter == 0:
        for i in dictionary:
            keys.append(i)
    counter += 1
    dict_list.append(dictionary)

# User input for key
print('Select one of the following keys: ')
for key in keys:
    print(key, end=' ')
key_in = input('\n')
while key_in not in keys:
    print('Please, select one of the following keys only: ')
    for key in keys:
        print(key, end=' ')
    key_in = input('\n')

key_values = []

# Incrementing list with each value of all the dictionaries' selected key
for dict1 in dict_list:
    for x in dict1:
        if x == key_in:
            key_values.append(dict1[key_in])

# Most common value and max/min value of the list
most_common = Counter(key_values).most_common(1)
max1 = max(key_values)
min1 = min(key_values)

print('Most common value between keys: ')
print(most_common[0], "\n")
print('Max value between keys: ')
print(max1, "\n")
print('Minimum value between keys: ')
print(min1)
