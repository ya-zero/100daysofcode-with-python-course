"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

tmp = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(tmp, 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)

with open(DICTIONARY) as f:
    loglines = f.readlines()

for i in loglines:
    print (i)
