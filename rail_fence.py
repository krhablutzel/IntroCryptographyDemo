"""
Rail Fence Cipher Encoder
Input:
- A Message (letters [a-z] and [A-Z])
- A Rail Count (Integer 2+)
- A Mode (encrypt (e) or decrypt (d))

Output:
- Encoded/decoded Message (letters (un)scrambled along fence rails)
"""
def main():
    verbose = True  # show pattern of letters on the rails

    ### Input

    # get message from user
    msg = input("Message: ")

    # get rail count from user
    rail_count = input("Rail Count: ")
    rail_count = clean_rail_input(rail_count)  # convert rail count to number

    # get mode from user
    mode = get_mode()

    # encrypt message
    if mode == 0:
        # remove spaces for encrypt
        msg = clean_string_input(msg, remove_spaces=True)  # clean input to contain only letters
        rail_cipher_encrypt(msg, rail_count, verbose)
    # decrypt message
    elif mode == 1:
        # respect spaces for decrypt
        msg = clean_string_input(msg, remove_spaces=False)  # clean input to contain only letters
        rail_cipher_decrypt(msg, rail_count, verbose)


### Helper Functions
def clean_string_input(msg, remove_spaces=True):
    """Keep only alphabetical letters (A-Z) in message (optional: leave spaces)"""
    if remove_spaces:
        msg = ''.join(l for l in msg if l.isalpha()).upper()
    else:
        msg = ''.join(l for l in msg if (l.isalpha() or l == " ")).upper()

    return msg

def clean_rail_input(rail_count):
    """Convert rail_count from str to integer, and enforce 3+ value"""
    if rail_count.replace("-", "").isnumeric():
        rail_count = int(rail_count)
    else:
        # if rail_count isn't an integer, set default value to avoid errors
        print("Invalid input.")
        rail_count = 3

    # enforce 2+ value
    if rail_count < 2:
        print("Invalid input.")
        rail_count = 3  # default value

    return rail_count

def get_mode():
    # prompt user for mode (encrypt, decrypt)
    mode_in = input("Encrypt ('e') or decrypt ('d')?: ").lower()
    encrypt_terms = ["e", "encrypt", "encript", "0"]
    decrypt_terms = ["d", "decrypt", "decript", "1"]
    # try again on input if the user enters something wrong
    while (mode_in not in encrypt_terms) and (mode_in not in decrypt_terms):
        print('invalid mode. try again.')
        mode_in = input("Encrypt ('e') or decrypt ('d')?: ").lower()
    # translate string to encrypt/decrypt/brute force mode
    if mode_in in encrypt_terms:
        return 0
    elif mode_in in decrypt_terms:
        return 1
    else:
        # default case - should never reach, if input cleaning succeeds
        return 0

def calculate_rail_position(index, rail_count):
    """For a msg letter at index, and for a given rail_count
    return which rail the letter belongs on"""
    n = rail_count - 1

    # e.g. for 3 rails, indices are 0,1,2,1,0,1,2,1,...
    # this function is a combination of absolute values and mods
    # starts at 0, increases to rail_count-1, decreases to 0, and repeats
    return abs(((index+n)%(2*n))-n)

def render_rail(rail_items, rail_num, rail_count):
    """Format rail with correct spacing for printing"""
    # top and bottom rail - even spacing
    if rail_num == 0 or rail_num == (rail_count - 1):
        filler = " "*(rail_count*2-3)  # equals cycle-1
        rail_text = filler.join(rail_items)
    # inner rails - 2 spacings, and vary based on rail number 
    else:
        # don't ask me to explain these spacings...
        # I trial-and-error'ed it out...
        n = rail_count-1
        filler_ind = (2*(n-rail_num) - 1)
        filler1 = " " * filler_ind
        filler2 = " " * (2*n - filler_ind - 2)
        # create rail text
        rail_text = ""
        for i in range(len(rail_items)):
            # alternate between the two filler spacings
            if i % 2 == 0:
                rail_text += rail_items[i] + filler1
            else:
               rail_text += rail_items[i] + filler2 

    # shift start by rail number
    pad = " " * rail_num
    
    return pad + rail_text

def rail_cipher_encrypt(msg, rail_count, verbose=True):
    """Encode msg using rail cipher with 2+ rails"""
    ### Encoding
    # for each letter in msg, add to fence rail
    if verbose:
        print(f"Performing Rail Fance Cipher with {rail_count} rails.")

    # create list of lists to hold fence rails
    rails = [[] for i in range(rail_count)]

    # place letters on rails
    cycle = (rail_count * 2) - 2
    for i in range(len(msg)):
        # find which rail to place the letter, based on its position
        rail = calculate_rail_position(i, rail_count)

        # append the letter to its rail
        rails[rail].append(msg[i])

    # create ciphertext by appending rails
    c_text = " ".join(["".join(rail_items) for rail_items in rails])

    ### Output
    # print rails
    if verbose:
        for rail in range(rail_count):
            print(render_rail(rails[rail], rail, rail_count))

    # print msg and ciphertext
    print("Plaintext: ", msg)
    print("Ciphertext:", c_text)

def rail_cipher_decrypt(msg, rail_count, verbose=True):
    """Decode msg using rail cipher with 2+ rails"""
    if verbose:
        print(f"Decoding Rail Fance Cipher with {rail_count} rails.")
    ### Decoding
    # find fence rails
    # TODO: more complex rail-finding algorithm (when spaces not available)
    rail_strings = msg.split(" ")
    rails = [[x for x in y] for y in rail_strings]  # list of lists of letters

    # print letters from each rail
    if verbose:
        for rail in range(rail_count):
            print(render_rail(rails[rail], rail, rail_count))


# run main when we run this script
main()
