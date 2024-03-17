# RLE Image Encoder

## Description

The `rle-with-images` project is a set of routines developed for encoding and decoding image data using Run-Length Encoding (RLE). Run-Length Encoding is a simple form of data compression where consecutive identical elements (runs) are replaced by a count and a single instance of the element. This project focuses on optimizing datasets with repeated elements, particularly suited for image data where adjacent pixels often have similar values.

## Features

- **Encoding and Decoding:** Provides functions for encoding image data into RLE format and decoding RLE data back to its original form.
- **Hexadecimal Representation:** Includes functions to convert data between hexadecimal strings and numerical representations to enhance data portability and storage efficiency.
- **Menu-Driven Interface:** The project offers a user-friendly menu-driven interface for easy interaction with the encoding and decoding functionalities.
- **Integration with ConsoleGfx:** Utilizes the `ConsoleGfx` module for loading image files, displaying images, and performing test operations.

## Key Functions

- `encode_rle(flat_data)`: Encodes flat image data into RLE format.
- `decode_rle(data_string)`: Decodes RLE data string into flat image data.
- `to_hex_string(data)`: Converts numerical data to hexadecimal string representation.
- `to_rle_string(rle_string)`: Converts RLE data to a human-readable string format.
- `string_to_data(data_string)`: Converts hexadecimal string data to numerical representation.
- `string_to_rle(rle_string)`: Converts RLE string data to numerical representation.

## Usage

1. **Encoding Image Data:** Users can encode image data into RLE format using the provided functions. This allows for efficient storage and transmission of image data.
2. **Decoding RLE Data:** RLE-encoded data can be decoded back to its original form, enabling reconstruction of the image.
3. **Menu-Driven Interface:** Users can interact with the functionalities through a menu-driven interface, making it intuitive to use.
4. **Integration with ConsoleGfx:** The project seamlessly integrates with the `ConsoleGfx` module, enabling the loading and display of image data within the console environment.

## How to Run

To run the `rle-with-images` project, follow these steps:

1. Ensure all required Python modules are installed, including `ConsoleGfx`.
2. Run the `main()` function from the provided script.
3. Follow the on-screen menu prompts to perform encoding, decoding, and other operations as desired.

## Contributors

This project was developed by Jorge Garcia.

Contributions to the `rle-with-images` project are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to submit a pull request. 

## License

This project is licensed under the [MIT License](LICENSE) 
