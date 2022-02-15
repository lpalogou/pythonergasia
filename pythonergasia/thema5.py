import re
from collections import Counter

# Reading the file
with open('two_cities_ascii.txt', 'r') as f:
    content = f.read().lower().split()  # Read all the content, lower it and split its spaces and new lines
f.close()

text = []
counter = 0
pattern = re.compile('[^a-z]')  # Regex pattern
for word in content:
    result = re.sub(pattern, '', content[counter])
    content[counter] = result
    text.append(content[counter])
    counter += 1

text_twos = []
text_threes = []

# 10 most common words
most_common_words = Counter(text).most_common(10)

# For every word, we append the first 2/3 characters of the word,
for i in range(len(text)):
    if len(text[i]) > 1:
        text_twos.append(text[i][0:2])
    if len(text[i]) > 2:
        text_threes.append(text[i][0:3])

# then we find the most common 2/3-letter combinations
most_common_twos = Counter(text_twos).most_common(3)
most_common_threes = Counter(text_threes).most_common(3)

print('10 most common words: ')
print(most_common_words, '\n')
print('3 most common initial 2-letter combinations: ')
print(most_common_twos, '\n')
print('3 most common initial 3-letter combinations: ')
print(most_common_threes)
