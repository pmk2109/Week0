from collections import defaultdict


def substring_old(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    return [sub for word in words for sub in substrings if sub in word]


def substring_new(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''

    """
    d = defaultdict(str)
    for word in set(words):
        for sub in set(substrings):
            if sub in word:
                print sub
                d[sub]+=word
    return d
    """


    s = set()
    for word in words:
        for i in xrange(len(word)-2):
            substr = word[i:i+3]
            s.add(substr)
    return [substr for substr in substrings if substr in s]
