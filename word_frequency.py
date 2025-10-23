#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


def get_sentence():
    user_sentence = input("Enter a sentence: ")
    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    return user_sentence
            
def calculate_frequencies(sentence):
    s = []
    q = []
    s.append(sentence.split(' '))
def print_frequencies(words, frequencies):
    print("Hi")
    
def main():
    given = get_sentence()
    calculate_frequencies(given)
    print("Done")
    
main()
