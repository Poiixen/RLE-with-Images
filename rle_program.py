from console_gfx import ConsoleGfx

# FIXME define functions to work with menu options

def hex_char_decode(digit):
    dec = 0 # define the variable
    if digit == "0":
        dec = 0
    if digit == "1":
        dec = 1
    if digit == "2":
        dec = 2
    if digit == "3":
        dec = 3
    if digit == "4": # follow conversion table, result is integer
        dec = 4
    if digit == "5":
        dec = 5
    if digit == "6":
        dec = 6
    if digit == "7":
        dec = 7
    if digit == "8":
        dec = 8
    if digit == "9":
        dec = 9
    if digit == "A" or digit == "a": # detects input from capital and lowercase "A" with proper conversion
        dec = 10
    if digit == "B" or digit == "b":
        dec = 11
    if digit == "C" or digit == "c":
        dec = 12
    if digit == "D" or digit == "d":
        dec = 13
    if digit == "E" or digit == "e":
        dec = 14
    if digit == "F" or digit == "f":
        dec = 15
    return dec


def to_hex_string(data):
    result = 0
    if data[0] == "0" and (data[1] == "x" or data[1] == "b"):  # detects whether first and second term start with "0x" or "0b"
        data = data[2:]  # if true, skips to second index
    else:
        data = data[0:] # if false, remain the same
    bit_index = len(data) - 1
    for digit in data: # this loop iterates through each digit from input into the function hex_char_decode, repeating until there are no more digits
        result += hex_char_decode(digit) * 16 ** bit_index 
        bit_index -= 1 
    return result

def count_runs(flat_data):
    pass

def encode_rle(flat_data):
    pass

def get_decoded_length(rle_data):
    pass

def decode_rle(data__string):
    pass

def string_to_data(data_string):
    pass



# define a function that prints menu to improve readibility
def menu():
    print(
        "RLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String",
        "\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data",
    )


# define a function that will fix zybooks import error
def main():
    # display welcome message
    print("\nWelcome to the RLE inmage encoder!")

    # this function displays the spectrum
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    image_data = None
    print(to_hex_string([3, 15, 6, 4]))
    while True:
        menu()
        option = int(input("\nSelect a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            # loads filename entered by user
            image_data = ConsoleGfx.load_file(input("Enter name of file to load:"))
            pass
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            # display image_data
            ConsoleGfx.display_image(image_data)
            pass


if __name__ == "__main__":
    main()



