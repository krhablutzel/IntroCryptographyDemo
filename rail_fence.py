"""
Rail Fence Cipher Encoder
Input:
- A Message (letters [a-z] and [A-Z])
- A Rail Count (Integer 2+)

Output:
- Encoded Message (letters scrambled along fence rails)
"""
def main():
    verbose = True  # show pattern of letters on the rails

    ### Input

    # get message from user
    msg = input("Message: ")
    msg = clean_string_input(msg)  # clean input to contain only letters

    # get rail count from user
    rail_count = input("Rail Count: ")
    rail_count = clean_rail_input(rail_count)  # convert rail count to number
    
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
        edge_filler = " " * rail_count
        inner_filler = " " * (rail_count//2)

        # print rails
        for rail in range(rail_count):
            print(render_rail(rails[rail], rail, rail_count))

    # print msg and ciphertext
    print("Plaintext: ", msg)
    print("Ciphertext:", c_text)


### Helper Functions
def clean_string_input(msg):
    """keep only alphabetical letters (A-Z) in message"""
    msg = ''.join(l for l in msg if l.isalpha()).upper()

    return msg

def clean_rail_input(rail_count):
    """convert rail_count from str to integer, and enforce 3+ value"""
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

def calculate_rail_position(index, rail_count):
    """for a msg letter at index, and for a given rail_count
    return which rail the letter belongs on"""
    n = rail_count - 1

    # e.g. for 3 rails, indices are 0,1,2,1,0,1,2,1,...
    # this function is a combination of absolute values and mods
    # starts at 0, increases to rail_count-1, decreases to 0, and repeats
    return abs(((index+n)%(2*n))-n)

def render_rail(rail_items, rail_num, rail_count):
    """format rail with correct spacing for printing"""
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

# run main when we run this script
main()
