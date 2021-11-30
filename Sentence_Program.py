#                Program 1:
# This program will ask for a sentence as input.
# The number of words, vowels and consonants in the input will be displayed in the end.

sent_user = str(input("Enter your sentence: "))

def word_count():
    string_word = sent_user
    word_list = string_word.split()
    
    numb_words = len(word_list)
    print(f"Words: {numb_words}")
    return numb_words


def vowel_count():
    string_vowel = sent_user
    numb_vowels = 0
    lowercase_sent_v = string_vowel.lower()
    
    for char in lowercase_sent_v:
        if char in "aeiou":
            numb_vowels += 1
    print(f"Vowels: {numb_vowels}")
    return numb_vowels


def consonant_count():
    string_conso = sent_user
    numb_conso = 0
    lowercase_sent_c = string_conso.lower()
    
    for char in lowercase_sent_c:
        if char in "bcdfghjklmnpqrstvwxyz":
            numb_conso += 1
    print(f"Consonants: {numb_conso}")
    return numb_conso
    

def main_func():
    word_count()
    vowel_count()
    consonant_count()
    
    
main_func()

