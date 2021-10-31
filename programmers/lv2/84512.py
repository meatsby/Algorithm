# Lv2 5주차_모음사전

from itertools import product
def solution(word):
    vowels = 'AEIOU'
    vowels1 = list(vowels)
    vowels2 = [''.join(word) for word in list(product(vowels, repeat=2))]
    vowels3 = [''.join(word) for word in list(product(vowels, repeat=3))]
    vowels4 = [''.join(word) for word in list(product(vowels, repeat=4))]
    vowels5 = [''.join(word) for word in list(product(vowels, repeat=5))]
    vowel_dict = vowels1 + vowels2 + vowels3 + vowels4 + vowels5
    vowel_dict.sort()
    return vowel_dict.index(word) + 1