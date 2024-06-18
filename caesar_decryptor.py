"""
Brute Force Caesar Cipher Decryptor
Input:
- An Encrypted Message (letters [a-z] and [A-Z])
- Mode (Encrypt (e), Decrypt (d), Brute Force (b))

Output:
- Encrypt/Decrypt Mode: Encoded/decoded message
- Brute Force Mode: Decrypted message for each possible shift
"""
def main():
    # get message from user
    msg = input("Message: ")
    msg = clean_string_input(msg)  # clean input to contain only letters

    # get mode from user
    mode = get_mode()

    # encrypt message
    if mode == 0:
        shift = get_shift()
        c_text = caesar_encrypt(msg, shift, verbose=True)
        print("Plaintext: ", msg)
        print("Ciphertext:", c_text)
    # decrypt message
    elif mode == 1:
        shift = get_shift()
        p_text = caesar_encrypt(msg, (-1)*shift, verbose=True) # -shift to decrypt
        print("Ciphertext:", msg)
        print("Plaintext: ", p_text)
    # decrypt message with each potential shift
    elif mode == 2:
        for shift in range(26):
            c_text = caesar_encrypt(msg, (-1)*shift)  # -shift to decrypt
            print("Shift: ", shift)
            print(c_text)

def clean_string_input(msg):
    # keep only alphabetical letters (A-Z) in message
    msg = ''.join(l for l in msg if l.isalpha()).upper()

    return msg

def get_mode():
    # prompt user for mode (encrypt, decrypt, brute force)
    mode_in = input("Encrypt ('e'), decrypt ('d'), or brute force decrypt ('b')?: ").lower()
    encrypt_terms = ["e", "encrypt", "encript", "0"]
    decrypt_terms = ["d", "decrypt", "decript", "1"]
    brute_force_terms = ["b", "bf", "brute force", "bruteforce", "2"]
    # try again on input if the user enters something wrong
    while (mode_in not in encrypt_terms) and (mode_in not in decrypt_terms) and (mode_in not in brute_force_terms):
        print('invalid mode. try again.')
        mode_in = input("Encrypt ('e'), decrypt ('d'), or brute force decrypt ('b')?: ").lower()
    # translate string to encrypt/decrypt/brute force mode
    if mode_in in encrypt_terms:
        return 0
    elif mode_in in decrypt_terms:
        return 1
    elif mode_in in brute_force_terms:
        return 2
    else:
        # default case - should never reach, if input cleaning succeeds
        return 2

def get_shift():
    # get shift from user
    shift = input("Shift: ")
    return clean_int_input(shift)  # convert shift to number

def clean_int_input(shift):
    # convert shift from str to integer
    if shift.replace("-", "").isnumeric():
        shift = int(shift)
    else:
        # if shift isn't an integer, set default value to avoid errors
        shift = 0

    return shift

def to_int(letter):
    # convert to unicode (65-90)
    unicode = ord(letter)

    # translate to numbers 0-25
    new_int = unicode - 65

    return new_int

def from_int(int_c):
    # first, wrap numbers >25 around to lower numbers
    # 26 -> 0, 27 -> 1, 28 -> 2, etc.
    mod_c = int_c % 26

    # return to unicode numbers
    unicode = mod_c + 65

    # convert to letter
    new_letter = chr(unicode)

    return new_letter

def caesar_encrypt(msg, shift, verbose=False):
    # for each letter in msg, move over by shift
    c_text = ""
    for l in msg:
        int_l = to_int(l)  # letter -> number  (see functions below for more detail)
        int_c = int_l + shift  # letter + shift
        c = from_int(int_c)  # number -> new letter

        # add enciphered letter to the new message
        c_text += c  

        # print steps to the user
        if verbose:
            print(f"{l} -> {c} ({int_l} + {shift} -> {int_c % 26})")
            
    return c_text

main()
