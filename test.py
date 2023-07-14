
def to_rle_string(rle_string): #input to_rle_string([15, 15, 6, 4]) yields string "15f:64"
    output = ""
    conversion_dict = {10: "a:", 11: "b:", 12: "c:", 13: "d:", 14: "e:", 15: "f:"}
    if len(rle_string) % 2 == 0: # if even
        if rle_string[1] in conversion_dict:
            rle_string[1] = conversion_dict[rle_string[1]] # replaces second term with corrosponding dictionary value. ex: [15, 15] = [15, "f:"]
    if len(rle_string) % 2 == 1: # if odd
        if rle_string[2] in conversion_dict:
            rle_string[2] = conversion_dict[rle_string[2]]
    for element in rle_string: # adds every element in rle_string list to the output string, made possible with str() around the integers.
        output += str(element) 
    return output



def string_to_rle(rle_string): #15f:64 => [15, 15, 6, 4]
    output = []
    conversion_dict = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", "f": 15}
    rle_list = rle_string.split(":")
    for element in rle_list:
        if len(element) == 3: # splits 3 characters into 2 and one. ex: "15f" => "15" and "f"   
            output.append(int(element[:2]))
            if element[-1] in conversion_dict:
                output.append(conversion_dict[element[-1]])
            else:
                output.append(element[-1]) 
        elif len(element) == 2: # similarly splits into first char and last char if element == 2. ex: "2e" => "2" and "e
            output.append(int(element[0])) 
            if element[1] in conversion_dict:
                output.append(conversion_dict[element[1]])
            else:
                output.append(int(element[-1]))
        
    return output

def decode_rle(data_string):
    list = []
    for i in range(0, len(data_string), 2): # differentiates between even and odd indexes
        value = data_string[i + 1]  # value is what is getting repeated, every other number after the first index
        repeated_times = data_string[i] # repeated_times is how many times the value is counted in list, every other number starting with the first
        list.extend([value] * repeated_times)
    return list


print(decode_rle((string_to_rle(input("Enter an RLE string to be decoded:")))))