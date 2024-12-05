def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Modify content (example: convert to uppercase)
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been read from {input_filename} and written to {output_filename} successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")
    read_and_write_file(input_file, output_file)
