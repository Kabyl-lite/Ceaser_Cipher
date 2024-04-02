def caesar_cipher(text, shift):
    """Encrypts or decrypts text using a Caesar cipher."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
        else:
            new_char = char  # Preserve non-alphabetic characters
        result.append(new_char)
    return ''.join(result)

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_cipher(message, shift)
    decrypted_message = caesar_cipher(encrypted_message, -shift)

    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()