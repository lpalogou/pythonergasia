def to_Binary(char):
    bin_num, bin_arr = [], []
    for i in char:
        bin_num.append(ord(i))  # Returns the int representing the Unicode character
    for i in bin_num:
        bin_arr.append(int(bin(i)[2:]))  # Conversion to binary
    return bin_arr


def get_Max_Length(array, x, num):
    count = 0
    result1 = 0

    for i in range(0, x):

        # Reset count when wanted bit is not found
        if array[i] != num:
            count = 0

        # If wanted bit is found, increment count and update result if count becomes more
        else:
            # increase count
            count += 1
            result1 = max(result1, count)
    return result1


# Reading the file
with open('two_cities_ascii.txt', 'r') as f:
    content = f.read().lower().split()  # Read all the content, lower it and split its spaces and new lines
f.close()

max_zeros = 0
max_zeros_char = []
max_ones = 0
max_ones_char = []
max_binary_zeros = []
max_binary_ones = []


# Converting each word to binary character by character, printing them and then checking and updating the max zeros
# and max ones
for word in content:
    for c in range(len(word)):
        binary = to_Binary(word[c])
        print(word[c], '->', binary)
        ones = get_Max_Length(str(binary[0]), len(str(binary[0])), '1')
        zeros = get_Max_Length(str(binary[0]), len(str(binary[0])), '0')
        if ones > max_ones:
            max_ones = ones
            max_ones_char = word[c]
            max_binary_ones = binary
        if zeros > max_zeros:
            max_zeros = zeros
            max_zeros_char = word[c]
            max_binary_zeros = binary

print('\n')
print('Number of most consecutive ones: ', max_ones)
print('ASCII character: ', max_ones_char)
print('Binary: ', max_binary_ones, '\n')
print('Number of most consecutive zeros: ', max_zeros)
print('ASCII character: ', max_zeros_char)
print('Binary: ', max_binary_zeros)
