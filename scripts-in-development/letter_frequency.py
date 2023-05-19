"""
Letter Frequency Charts
Input:
- A Message (letters [a-z] and [A-Z])

Output:
- A chart showing frequency of each letter in the message

"""
import matplotlib.pyplot as plt

def main():
    msg = clean_string_input(input("Message: "))
    print(msg)

    # get frequency for each letter in the alphabet
    alphabet, frequencies = count_letters(msg)

    # plot here
    print(alphabet)
    print(frequencies)



### Helper Functions
def clean_string_input(msg):
    # keep only alphabetical letters (A-Z) in message
    msg = ''.join(l for l in msg if l.isalpha()).upper()
    
    return msg

def count_letters(msg):
    # store counts of letters in dictionary
    # {letter: count, letter2: count2, etc.}
    counts = {}

    # for each letter, add 1 to the letter's count
    # unless: letter hasn't been seen yet. then,
    # initialize a count for that letter at 1
    for c in msg:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    # create list of each letter in the alphabet in order
    alphabet = [chr(65 + i) for i in range(26)]

    # create list of frequency for each letter in the alphabet
    frequencies = []
    for c in alphabet:
        if c in counts:
            # if letter was counted, use count
            frequencies.append(counts[c])
        else:
            # if letter wasn't counted, use 0
            frequencies.append(0)

    return alphabet, frequencies

main()
