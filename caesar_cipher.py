def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

output = caesar_cipher(message, shift, mode)
print("Result:", output)