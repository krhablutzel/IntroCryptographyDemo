"""
Brute Force Caesar Cipher Decryptor
Input:
- An Encrypted Message (letters [a-z] and [A-Z])

Output:
- Decoded Messages for each possible shift
"""
def main():
    # get message from user
    msg = input("Message: ")
    msg = clean_string_input(msg)  # clean input to contain only letters

    # decrypt message with each potential shift
    for shift in range(26):
        c_text = caesar_encrypt(msg, (-1)*shift)  # -shift to decrypt
        print("Shift: ", shift)
        print(c_text)
        

def clean_string_input(msg):
    # keep only alphabetical letters (A-Z) in message
    msg = ''.join(l for l in msg if l.isalpha()).upper()

    return msg

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
