# Write a program to implement Vigenere polyalphabetic cipher for messages composed from the letters
# of the English alphabet, the numerals 0 through 9, and the punctuation marks ‘.’, ‘,’, and ‘?’.

def vigenere_cipher(text, key):
    encrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha() or char.isdigit() or char in ['.', ',', '?']:
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + ord(key[key_index % key_length].upper()) - 65) % 26 + 65)
            elif char.islower():
                encrypted_text += chr((ord(char) - 97 + ord(key[key_index % key_length].lower()) - 97) % 26 + 97)
            elif char.isdigit():
                encrypted_text += chr((ord(char) - 48 + ord(key[key_index % key_length].lower()) - 97) % 10 + 48)
            else:
                encrypted_text += chr((ord(char) - 46 + ord(key[key_index % key_length].lower()) - 97) % 3 + 46)
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text


# Example usage:
message = input("Enter message to be encrypted:")
key = input("Enter SECRET key:")
encrypted_message = vigenere_cipher(message, key)
print("Encrypted message:", encrypted_message)
