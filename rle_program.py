<<<<<<< HEAD
print("test")
=======
from console_gfx import ConsoleGfx


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
>>>>>>> d8b7b24bff5df436904f76bf2139366f52597731
