
desition = input("Quiere encriptar(e) o desencriptar(d) el texto: ")
custom_key = 'happycoding'


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        if not char.isalpha():
            final_message += char

        else:
            #Para que no se pase de la longitud
            key_char = key[key_index % len(key)]
            #Después de usar una letra de la clave, subes el índice para la siguiente vuelta
            key_index += 1
            #print(f"{key_char} = {key} [ {key_index} % {len(key)}] \n")

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            #print(f"new_index = {index} + {offset} * {direction} = {new_index}")
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)


if desition == 'e':
    text = input("Ingrese el msg que quiere encriptar: ")
    encrypted = encrypt(text, custom_key)
    print(f'\nEncrypted text: {encrypted}\n')


if desition == 'd':
    text = input("Ingrese el msg que quiere desencriptar: ")
    decrypted = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decrypted}\n')

print(f'Key: {custom_key}')


