# Write a program to implement RSA cryptosystem. It should be a menu driven program with options of
# encryption or decryption. The values of p, q e, plaintext and cipher text should be entered from key-
# board.
import math

def gcd(a, b):
    # Calculate the greatest common divisor of a and b
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    # Calculate the modular multiplicative inverse of a modulo m
    if gcd(a, m) != 1:
        return None
    _, x, _ = extended_gcd(a, m)
    return x % m

def extended_gcd(a, b):
    # Extended Euclidean algorithm to calculate the Bézout coefficients
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def encrypt(plaintext, e, n):
    # Encrypt the plaintext using the public key (e, n)
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

def decrypt(ciphertext, d, n):
    # Decrypt the ciphertext using the private key (d, n)
    plaintext = ''.join([chr((char ** d) % n) for char in ciphertext])
    return plaintext

# Menu function for the program
def menu():
    print("RSA Cryptosystem")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

# Driver code
while True:
    menu()
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        # Encryption
        p = int(input("Enter the prime number p: "))
        q = int(input("Enter the prime number q: "))
        e = int(input("Enter the public exponent e: "))
        plaintext = input("Enter the plaintext: ")

        # Calculate n and φ(n)
        n = p * q
        phi_n = (p - 1) * (q - 1)

        # Check if e is coprime with φ(n)
        if gcd(e, phi_n) != 1:
            print("Invalid public exponent e.")
            continue

        # Encrypt the plaintext
        ciphertext = encrypt(plaintext, e, n)

        print("Encrypted ciphertext:", ciphertext)

    elif choice == 2:
        # Decryption
        p = int(input("Enter the prime number p: "))
        q = int(input("Enter the prime number q: "))
        d = int(input("Enter the private exponent d: "))
        ciphertext = list(map(int, input("Enter the ciphertext (space-separated): ").split()))

        # Calculate n
        n = p * q

        # Decrypt the ciphertext
        plaintext = decrypt(ciphertext, d, n)

        print("Decrypted plaintext:", plaintext)

    elif choice == 3:
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option (1-3).")
