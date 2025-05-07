text = str(input('Enter your Message: '))
shift = 3
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            index = alphabet.index(char) + key
            final_message += alphabet[index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {shift}')
decryption = decrypt(text, shift)
print(f'\nDecrypted text: {decryption}\n')