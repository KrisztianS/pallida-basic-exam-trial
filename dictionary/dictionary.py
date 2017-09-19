dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'
hun_word = "tojas"
eng_word = "egg"

def add_word(hun_word, eng_word):
    dictionary.append({hun_word: eng_word})
    print(dictionary)
# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    pass


def translate_to_eng(hun_word):
    pass

add_word(hun_word, eng_word)