"""
Caesar Cipher Encoder
Input:
- A Message (letters [a-z] and [A-Z])
- A Shift (Integer)

Output:
- Encoded Message (each letter shifted over by <shift> letters)
"""
def main():
    verbose = True  # show each letter as it's encoded

    ### Input

    # get message from user
    msg = input("Message: ")
    msg = clean_string_input(msg)  # clean input to contain only letters

    # get shift from user
    shift = input("Shift: ")
    shift = clean_int_input(shift)  # convert shift to number
    
    ### Encoding

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
            # print(f"Encoding {l} ({int_l}) by shift {shift}")
            print(f"{l} -> {c} ({int_l} + {shift} -> {int_c % 26})")
            # print(f"> {c_text}", end="\n\n")


    ### Output

    # print msg and ciphertext
    print("Plaintext: ", msg)
    print("Ciphertext:", c_text)


### Helper Functions
def clean_string_input(msg):
    # keep only alphabetical letters (A-Z) in message
    msg = ''.join(l for l in msg if l.isalpha()).upper()

    return msg

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

# run main when we run this script
main()
