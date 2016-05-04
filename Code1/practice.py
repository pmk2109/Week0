from examples import is_palindrome
import numpy as np


def sum_ints(lst):
    '''
    INPUT: list
    OUTPUT: int

    The input list contains a mixture of integers, floats and strings. Sum up
    only the ints.
    Hint: Use the isinstance function.
    '''
    return sum([x for x in lst if isinstance(x, int)])


def min_and_max(lst):
    '''
    INPUT: list
    OUTPUT: tuple of two ints/floats

    Given a list of ints and/or floats, return a 2-tuple containing the values
    of the items with the smallest and largest absolute values.

    In the case of an empty list, return None.
    '''
    if not lst:
        return
    else:
        minx = np.argmin(np.absolute(lst))
        maxx = np.argmax(np.absolute(lst))
    return (lst[minx], lst[maxx])


def are_palindromes(words):
    '''
    INPUT: list
    OUTPUT: bool

    Given a list of strings, return whether ALL of the elements are
    palindromes.

    Hint: use the is_palindrome function that has been imported at
    the top of this file
    '''
    #for word in words:
    #    if not is_palindrome(word):
    #        return False
    #return True

    return all([False if not is_palindrome(word) else True for word in words])


def substring(words, substrings):
    '''
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    '''
    return [sub for word in words for sub in substrings if sub in word ]
