# error_handling.py

def read_user_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            print("\n--- File Content Start ---")
            print(file.read())
            print("--- File Content End ---\n")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Sample usage
if __name__ == "__main__":
    read_user_file()

