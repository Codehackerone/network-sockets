# Write a program to implement Columnar Transposition. Take two lines of text, and test your program.
import math


def columnar_transposition_encrypt(message, key):
    # Determine the number of columns based on the key length
    num_columns = len(key)

    # Add padding to the message if needed
    num_padding = num_columns - (len(message) % num_columns)
    message += ' ' * num_padding

    # Create the transposition matrix
    matrix = [list(message[i:i + num_columns]) for i in range(0, len(message), num_columns)]

    # Sort the columns based on the alphabetical order of the key
    sorted_columns = sorted(enumerate(key), key=lambda x: x[1])

    # Read out the columns in the sorted order to obtain the transposed message
    transposed_message = ''.join(matrix[row][col] for col, _ in sorted_columns for row in range(len(matrix)))

    return transposed_message


# Example usage
message = input("Enter the message: ")
key = input("Enter the key: ")

encrypted_message = columnar_transposition_encrypt(message, key)
print("Encrypted message:", encrypted_message)