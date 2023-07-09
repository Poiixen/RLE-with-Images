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


def count_runs(flat_data):
    list = []
    for num in flat_data:
        if num not in list:  # checks if num is previously in list
            list.append(num)  # if not in list, adds num

    return len(list)  # returns unique amount of integers passed through





def encode_rle(flat_data):
    pass


def get_decoded_length(rle_data):
    pass


def decode_rle(data__string):
    pass


def string_to_data(data_string):
    pass


print(to_hex_string([3, 15, 6, 4]))
print(count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]))