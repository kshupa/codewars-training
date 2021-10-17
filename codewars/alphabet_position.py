# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.


def alphabet_position(string):
    alphabet = [
        a,
        b,
        c,
        d,
    ]

    for letter in string:
        if letter in alphabet.keys():
            result = empty.join(alphabet[letter])

    return result


# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

print(alphabet_position("The"))
