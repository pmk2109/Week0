from string import punctuation
from collections import Counter
import numpy as np

def invalid_words(wordlist, document_filename):
    '''
    INPUT: list, str
    OUTPUT: int

    Given a list of all the valid words and a document filename, return a list
    of words from the document that are not valid words.
    '''
    wordlist_set = set(wordlist)
    with open(document_filename) as doc:
        result = []
        for line in doc:
            words = line.strip().split()
            for word in words:
                if word.lower().strip(punctuation) not in wordlist_set:
                    result.append(word)
        return result


def common_characters(s, num):
    '''
    INPUT: str, int
    OUTPUT: list of chars

    Return the list of characters which appear in the string s more than num
    times.
    '''
    result = []
    c = Counter(s)
    """
    for char in s:
        if s.count(char) > num:
            if char not in result:
                result.append(char)
    """
    """
    for k, v in c.iteritems():
        if v>num:
            result.append(k)
    return result
    """

    return [k for k, v in c.iteritems() if v>num]


def sum_to_zero(lst):
    '''
    INPUT: list of ints
    OUTPUT: tuple of two ints

    Return a tuple of two values from the input list that sum to zero.
    If none exist, return None.
    '''
    """
    for i, item1 in enumerate(lst):
        for item2 in lst[i + 1:]:
            if item1 + item2 == 0:
                return item1, item2

    c = Counter(lst)
    for item in c:
        if (c[item] - item) == 0:
            return c[item], item
    """

    s = Counter(lst)
    for i in lst:
        if i == 0 and s[i] >1:
            return (0,0)
        elif -i in s:
            return (i, -i)
