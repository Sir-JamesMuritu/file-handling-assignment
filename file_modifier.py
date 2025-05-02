# file_rw.py

def read_and_modify_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Example modification: Convert to uppercase

        with open(destination_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content successfully written to {destination_file}")

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except IOError:
        print("Error: An error occurred while reading or writing the file.")


# Sample usage
if __name__ == "__main__":
    read_and_modify_file('input.txt', 'output.txt')

