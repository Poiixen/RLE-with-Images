def to_hex_string(data):
    output = ""
    for num in data:  # this for loop changes numbers in list accordingly , and adds change to output string
        if num < 10 or num > 15:
            output += str(num)
        if num == 10:
            output += "a"
        if num == 11:
            output += "b"
        if num == 12:
            output += "c"
        if num == 13:
            output += "d"
        if num == 14:
            output += "e"
        if num == 15:
            output += "f"
    return output


def count_runs(flat_data): # counts unique amount of runs that passes through function
    runs = 1
    count = 1
    current = flat_data[0]
    for num in flat_data[1:]:
        if count >= 15: # breaks off into a new run if the count is more than 15, resetting the count 
            runs += 1
            count = 1
        if current == num: 
            count += 1
        else:
            count = 1 # if current is unequal to the number, changes the current to new number, while resetting the count
            current = num
            runs += 1

    return runs

print(count_runs([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]))



def encode_rle(flat_data):
    pass


def get_decoded_length(rle_data):
    pass


def decode_rle(data__string):
    pass


def string_to_data(data_string):
    pass


print(to_hex_string([3, 15, 6, 4]))
