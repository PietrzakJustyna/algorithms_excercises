#!/usr/bin/env python
# -*- coding: utf-8 -*-

# palindrom


def check_if_palindrom(sentence):
    return sentence.lower().replace(" ", "") == sentence.lower().replace(" ", "").decode("utf-8")[::-1].encode("utf-8")


print(check_if_palindrom("kajak"))
print(check_if_palindrom("Kajak"))
print(check_if_palindrom("nie"))
print(check_if_palindrom("Kobyła ma mały bok"))
print(check_if_palindrom("Nie jest to palindrom"))


print("")


def check_if_has_same_letters(word1, word2):
    return sorted(word1) == sorted(word2)


print(check_if_has_same_letters("mama", "aamm"))

