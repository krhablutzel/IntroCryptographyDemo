"""
Vigenere Cipher Encoder
Input:
- A Message (letters [a-z] and [A-Z])
- A Keyword (letters [a-z] and [A-Z])

Output:
- Encoded Message (each letter shifted over by corresponding letter in the keyword)
"""

def main():
    verbose = True  # show each letter as it's encoded

    ### Input

    # get message from user
    msg = input("Message: ")
    msg = clean_string_input(msg)  # clean input to contain only letters

    # get shift from user
    keyword = input("Keyword: ")
    keyword = clean_string_input(keyword)  # clean keyword to contain only letters

    
    ### Encoding

    # for each letter in msg, shift over by corresponding letter in the key
    c_text = ""
    for i in range(len(msg)):
        # which letters to use
        l = msg[i]  # 0th letter, 1st letter, 2nd letter, etc.
        k = keyword[i % len(keyword)]  # after last letter, wrap around to first letter

        # convert to numbers
        int_l = to_int(l)
        int_k = to_int(k)

        # sum of letter + key_letter = cipher_letter
        int_c = int_l + int_k  # letter + key_letter
        c = from_int(int_c)  # covert number to enciphered letter

        # add enciphered letter to the new message
        c_text += c  

        # print steps to the user
        if verbose:
            # print(f"Encoding {l} ({int_l}) by shift {k} {int_k}")
            print(f"{l} + {k} -> {c} ({int_l} + {int_k} -> {int_c % 26})")
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
