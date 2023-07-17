from console_gfx import ConsoleGfx


def to_hex_string(data):
    output = ""
    for num in data:  # this for checks every number in data, adding each number after conversion to output string
        if int(num) < 10 or int(num) > 15:
            output += str(num)
        elif num == 10:   # for numbers less than 10 or greater than 15, they stay the same
            output += "a" # numbers between 10 and 15 changes the num input to its letter equivalent
        elif num == 11:
            output += "b" 
        elif num == 12:
            output += "c"
        elif num == 13:
            output += "d"
        elif num == 14:
            output += "e"
        elif num == 15:
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

def encode_rle(flat_data):
    list = []
    count = 1
    current = flat_data[0]
    for num in flat_data[1:]:   
        if current == num:  # if current is equal to num, count increments by 1 until current is != to num
            count += 1
        else:
            if count >= 15: # when unequal, if count exceeds 15, appends '15' and current to list, while maintaining loop
                list.append(15)
                list.append(current)
                count -= 15
                while count >= 15: # infinite loop until count is under 15, then adds that value with current to list
                    list.append(15)
                    list.append(current)
                    count -= 15
                if count > 0: 
                    list.append(count)
                    list.append(current)
            else:
                list.append(count)
                list.append(current)
            count = 1
            current = num
    if count >= 15: # this if-else was made to include the last digit, which is missed by the for loop 
        list.append(15)
        list.append(current)
        count -= 15
        while count >= 15: # same as above while loop, prepares for a test case in which there are countless amounts of the same integer
            list.append(15)
            list.append(current)
            count -= 15
        if count > 0:
            list.append(count)
            list.append(current)
    else:
        list.append(count)
        list.append(current)
    return list

def get_decoded_length(rle_data): # function gets the length of the rle_data input
    length = 0
    current = rle_data[0] 
    for num in rle_data[0::2]: # only saves every other number, adding it to length variable.
        length += num
    return length 

def decode_rle(data_string):
    list = []
    for i in range(0, len(data_string), 2): # differentiates between even and odd indexes
        value = data_string[i + 1]  # value is what is getting repeated, every other number after the first index
        repeated_times = data_string[i] # repeated_times is how many times the value is counted in list, every other number starting with the first
        list.extend([value] * repeated_times)
    return list


def string_to_data(data_string): 
    list = []
    for char in data_string: # iterates through input string, and replaces letter to num equivalent
        if char == "a" or char == "A":
            list.append(10)
        elif char == "b" or char == "B":
            list.append(11)
        elif char == "c" or char == "C": 
            list.append(12)
        elif char == "d" or char == "D":
            list.append(13)
        elif char == "e" or char == "E":
            list.append(14)
        elif char == "f" or char == "F":
            list.append(15)
        else:
            list.append(int(char)) # if it is not a letter, it appends the integer version of char
    return list 

def to_rle_string(rle_string): #input to_rle_string([15, 15, 6, 4]) yields string "15f:64"
    output = ""
    conversion_dict = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    print(rle_string)
    for i, element in enumerate(rle_string):
        if i % 2 == 1:
            # Check if the element is in the conversion_dict
            if element in conversion_dict:
                element = conversion_dict[element]
            output += str(element) + ":"
        else:
            output += str(element)
    return output.rstrip(":") 

def string_to_rle(rle_string): #15f:64 => [15, 15, 6, 4]
    output = []
    conversion_dict = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
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
                output.append((element[-1]))
    return output



# define a function that prints menu to improve readibility
def menu():
    print(
        "RLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String",
        "\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data",
    )

# define a function that will fix zybooks import error
def main():
    # display welcome message
    print("\nWelcome to the RLE image encoder!")

    # this function displays the spectrum
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    image_data = None
    
    while True:
        menu()
        option = int(input("\nSelect a Menu Option: "))
        if option == 0:
            break
        elif option == 1: 
            # loads filename entered by user
            image_data = ConsoleGfx.load_file(input("Enter name of file to load:"))
        elif option == 2: 
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif option == 3: 
            image_data = decode_rle(string_to_rle(input("Enter an RLE string to be decoded:")))
        elif option == 4: 
            image_data = decode_rle(string_to_data(input("Enter the hex string holding RLE data:")))
        elif option == 5:
            image_data = string_to_data(input("Enter the hex string holding flat data:"))
        elif option == 6: 
            # display image_data
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
        elif option == 7: # something here does not register more than 2 or 3 characters 
            image_data = encode_rle(image_data)
            print(f"RLE representation: {to_rle_string(image_data)}")
            
        elif option == 8: 
            image_data = encode_rle(image_data)
            print(f"RLE hex values: {to_hex_string(image_data)}")

        elif option == 9: #wrong           
            print(f"Flat hex values: {to_hex_string(image_data)}")

        else:
            print("Error! Invalid input.") 

if __name__ == "__main__":
    main()


