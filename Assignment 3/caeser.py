# Write a program to implement CAESAR cipher (substitution cipher). The messages for encryption
# should be composed from the letters of the English alphabet, the numerals 0 through 9.

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # check if the character is a letter
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)  # encrypt uppercase letters
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)  # encrypt lowercase letters
        elif char.isdigit():  # check if the character is a digit
            encrypted_text += chr((ord(char) - 48 + shift) % 10 + 48)  # encrypt digits
        else:
            encrypted_text += char  # leave other characters unchanged
    return encrypted_text


# Example usage:
message = input("Enter message to be encrypted:")
shift_amount = int(input("Enter shift:"))
encrypted_message = caesar_cipher(message, shift_amount)
print("Encrypted message:", encrypted_message)
