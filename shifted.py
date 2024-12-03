def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():

            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            
            new_char = chr((ord(char) - start - shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result


text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Расшифрованный текст:", decrypted_text)
