"""
A pangram (Greek: pan gramma, "every letter") or holoalphabetic
sentence for a given alphabet is a sentence using every letter of the alphabet
at least once. Perhaps you are familiar with the well known pangram "The quick
brown fox jumps over the lazy dog".
For this mission, we will use the latin alpahabet (A-Z). You are given a text
with latin letters and punctuation symbols. You need to check if the sentence
is a pangram or not. Case does not matter.
"""
import string

ALL_LETTERS = "".join(string.ascii_lowercase)

def check_pangram(text):

    return len(ALL_LETTERS) == len(set([ch for ch in text.lower() if ch in string.ascii_letters]))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
