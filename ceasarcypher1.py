def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            shifted = (ord(char.lower()) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

message = input("Enter message: ")
shift_amount = int(input("Enter shift amount: "))

print("Encoded message:", caesar_cipher(message, shift_amount))
