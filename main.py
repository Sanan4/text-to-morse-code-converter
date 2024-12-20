# The length of a dot is one unit (".")
# A dash is three units ("---")
# The space between parts of a letter is one unit
# The space between letters is three units
# The space between words is seven units

character_to_morse = {

    "A": ". ---   ",
    "B": "--- . . .   ",
    "C": "--- . --- .   ",
    "D": "--- . .   ",
    "E": ".   ",
    "F": ". . --- .   ",
    "G": "--- --- .   ",
    "H": ". . . .   ",
    "I": ". .   ",
    "J": ". --- --- ---   ",
    "K": "--- . ---   ",
    "L": ". --- . .   ",
    "M": "--- ---   ",
    "N": "--- .   ",
    "O": "--- --- ---",
    "P": ". --- --- .   ",
    "Q": "--- --- . ---   ",
    "R": ". --- .   ",
    "S": ". . .   ",
    "T": "---   ",
    "U": ". . ---   ",
    "V": ". . . ---   ",
    "W": ". --- ---   ",
    "X": "--- . . ---   ",
    "Y": "--- . --- ---   ",
    "Z": "--- --- . .   ",

    " ": "       ",

    "0": "--- --- --- --- ---   ",
    "1": ". --- --- --- ---   ",
    "2": ". . --- --- ---   ",
    "3": ". . . --- ---   ",
    "4": ". . . . ---   ",
    "5": ". . . . .   ",
    "6": "--- . . . .   ",
    "7": "--- --- . . .   ",
    "8": "--- --- --- . .   ",
    "9": "--- --- --- --- .   "

}

user_word = input("Type a word/sentence: ")
user_word = user_word.upper()

word = list(user_word)

for i in word:
    print(character_to_morse[i])
