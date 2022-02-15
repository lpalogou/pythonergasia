from urllib.request import Request, urlopen
import ast


def get_Max_Length(array, x, num):
    count = 0
    result1 = 0

    for k in range(0, x):

        # Reset count when wanted bit is not found
        if array[k] != num:
            count = 0

        # If wanted bit is found, increment count and update result if count becomes more
        else:
            # increase count
            count += 1
            result1 = max(result1, count)
    return result1


# Requesting the data from the latest round
req = Request('https://drand.cloudflare.com/public/latest',
              headers={'User-Agent': 'Mozilla/5.0(Windows NT 6.1; WOW64; rv:31.0)Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()  # Reading the data
data = data.decode('utf-8')  # Decoding them into string data

dictionary = ast.literal_eval(data)  # Creates a dictionary from the data string
latest_round = dictionary['round']  # Gets latest round from dictionary
latest_randomness = dictionary['randomness']    # Gets latest randomness from dictionary

print('Latest Round: ', latest_round)
print('Latest Randomness value: ', latest_randomness, '\n')

max_zeros = 0
max_zeros_round = []
max_ones = 0
max_ones_round = []
max_binary_zeros = []
max_binary_ones = []

# Converting the whole latest hexadecimal value to binary and checking and updating the max zeros and max ones
binary = '{0:08b}'.format(int(latest_randomness, 16))
ones = get_Max_Length(str(binary), len(str(binary)), '1')
zeros = get_Max_Length(str(binary), len(str(binary)), '0')
if ones > max_ones:
    max_ones = ones
    max_ones_round = latest_round
    max_binary_ones = binary
if zeros > max_zeros:
    max_zeros = zeros
    max_zeros_round = latest_round
    max_binary_zeros = binary

# Requesting the data from the 99 rounds before the latest (for a total of 100 rounds wanted)
for i in range((latest_round-100), latest_round):
    req = Request('https://drand.cloudflare.com/public/' + str(i),
                  headers={'User-Agent': 'Mozilla/5.0(Windows NT 6.1; WOW64; rv:31.0)Gecko/20130401 Firefox/31.0'})
    new_data = urlopen(req).read()
    new_data = new_data.decode('utf-8')

    new_dictionary = ast.literal_eval(new_data)  # Creates a dictionary from the data string
    new_latest_round = new_dictionary['round']  # Gets latest round from dictionary
    new_latest_randomness = new_dictionary['randomness']  # Gets latest randomness from dictionary

    # Converting each hexadecimal value to binary and checking and updating the max zeros and max ones
    new_binary = '{0:08b}'.format(int(new_latest_randomness, 16))
    new_ones = get_Max_Length(str(new_binary), len(str(new_binary)), '1')
    new_zeros = get_Max_Length(str(new_binary), len(str(new_binary)), '0')
    if new_ones > max_ones:
        max_ones = new_ones
        max_ones_round = new_latest_round
        max_binary_ones = new_binary
    if new_zeros > max_zeros:
        max_zeros = new_zeros
        max_zeros_round = new_latest_round
        max_binary_zeros = new_binary

print('Number of most consecutive ones: ', max_ones)
print('Round: ', max_ones_round)
print('Binary: ', max_binary_ones, '\n')
print('Number of most consecutive zeros: ', max_zeros)
print('Round: ', max_zeros_round)
print('Binary: ', max_binary_zeros)
