import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows() if row.letter}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word:\n").upper()
wordlist = [phonetic_dict[letter] for letter in user_word]
print(wordlist)