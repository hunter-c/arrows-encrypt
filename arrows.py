import random

# function for encypting plain text
def encrypt(plaintext, key):
    ciphertext = ""
    shiftedtext = shift(plaintext, key, False)
    for c in shiftedtext:
        if ord(c) < 32 or ord(c) > 126:
            ciphertext += base4_to_ticks(dec_to_base4(95))
        else:
            ciphertext += base4_to_ticks(dec_to_base4(ord(c)))
    return ciphertext

# function for decrypting ciphertext
def decrypt(ciphertext, key):
    shiftedtext = ""
    characters = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
    for c in characters:
        shiftedtext += chr(base4_to_dec(ticks_to_base4(c)))
    return shift(shiftedtext, key, True)  # return plaintext


# generates key of length equal to the plaintext within printable text range
def generate_OTP_key(n):
    key = ""
    for i in range(n):
        key += chr(random.randrange(32, 127))
    return key


"""
standard viginere cipher that shifts text based on ascii table's printable values (the range 32-126 inclusive)
(e.g. a shift of 'a' is 97 not 0).
    plaintext: text to be shifted
    key: single or series of characters to shift text by
    reverse_shift: boolean value determining if shift should be forward or backward
"""
def shift(plaintext, key, reverse_shift):
    shifted_text = ""
    if not reverse_shift:   # forward shift
        for i in range(len(plaintext)):
            if ord(plaintext[i]) + (ord(key[i % len(key)]) - 32) > 126:
                shifted_text += chr((ord(plaintext[i]) +
                                     (ord(key[i % len(key)]) - 32)) - 95)
            else:
                shifted_text += chr((ord(plaintext[i]) +
                                     (ord(key[i % len(key)]) - 32)))
    else:   # backward shift
        for i in range(len(plaintext)):
            if ord(plaintext[i]) - (ord(key[i % len(key)]) - 32) < 32:
                shifted_text += chr((ord(plaintext[i]) -
                                     (ord(key[i % len(key)]) - 32)) + 95)
            else:
                shifted_text += chr((ord(plaintext[i]) -
                                     (ord(key[i % len(key)]) - 32)))
    return shifted_text

# simple dec to base for converter. Only works for numbers < 256
def dec_to_base4(number_dec):
    number_base4 = str(number_dec // 64)  # needs only 4 digits (0-256)
    number_base4 += str((number_dec % 64) // 16)
    number_base4 += str(((number_dec % 64) % 16) // 4)
    number_base4 += str(((number_dec % 64) % 16) % 4)
    return number_base4

# simle base4 to dec converter. Works only for numbers < 256
def base4_to_dec(number_base4):
    number_dec = eval(number_base4[0]) * (4 ** 3)
    number_dec += eval(number_base4[1]) * (4 ** 2)
    number_dec += eval(number_base4[2]) * (4 ** 1)
    number_dec += eval(number_base4[3]) * (4 ** 0)
    return number_dec

# maps the symbols to the base4 digits
def base4_to_ticks(number_base4):
    ticks = ""
    # for n in number_base4:
    #     if n == '0':
    #         ticks += '.'
    #     elif n == '1':
    #         ticks += ','
    #     elif n == '2':
    #         ticks += '\''
    #     elif n == '3':
    #         ticks += '`'
    # for n in number_base4:
    #     if n == '0':
    #         ticks += '♥'
    #     elif n == '1':
    #         ticks += '♣'
    #     elif n == '2':
    #         ticks += '♦'
    #     elif n == '3':
    #         ticks += '♠'

    for n in number_base4:
        if n == '0':
            ticks += '▴'
        elif n == '1':
            ticks += '▾'
        elif n == '2':
            ticks += '◂'
        elif n == '3':
            ticks += '▸'
    return ticks


def ticks_to_base4(ticks):
    number_base4 = ""
    # for n in ticks:
    #     if n == '.':
    #         number_base4 += '0'
    #     elif n == ',':
    #         number_base4 += '1'
    #     elif n == '\'':
    #         number_base4 += '2'
    #     elif n == '`':
    #         number_base4 += '3'
    for n in ticks:
        if n == '▴':
            number_base4 += '0'
        elif n == '▾':
            number_base4 += '1'
        elif n == '◂':
            number_base4 += '2'
        elif n == '▸':
            number_base4 += '3'
    return number_base4



def encryptor(encrypt_decrypt, use_OTP=False, key='', text=''):
    result = ""

    if encrypt_decrypt == 1:
        if use_OTP:
            key = generate_OTP_key(len(text))
        result = encrypt(text, key)

    elif encrypt_decrypt == 2:
        result = decrypt(text, key)
    
    return (result, key)


# def main():
#     while(True):
#         user_in = input("Would you like to encrypt or decrypt? (e/d): ")
#         if user_in == 'e':
#             print("===============================================================")
#             plaintext = input("Enter text to encrypt:\n")
#             user_in = input("\nGenerate one time pad key? (y/n): ")
#             if user_in == 'y':
#                 key = generate_OTP_key(len(plaintext))
#                 print(f"\nGenerated key:\n{key}")
#             else:
#                 key = input("\nEnter key:\n")
#             print("\nCiphertext:")
#             print(encrypt(plaintext, key))
#             print("===============================================================\n")
#         elif user_in == 'd':
#             print("===============================================================")
#             ciphertext = input("Enter text to decrypt:\n")
#             key = input("\nEnter key:\n")
#             print("\nplaintext:")
#             print(decrypt(ciphertext, key))
#             print("===============================================================\n")
#         else:
#             print("Input not recognized...\n")


# if __name__ == "__main__":
#     main()