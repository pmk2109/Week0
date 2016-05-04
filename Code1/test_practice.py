import nose.tools as n
import practice


def get_message(result, expected):
    message = 'Incorrect result. You returned {0} instead of {1}.'
    return message.format(result, expected)


def test_sum_ints():
    result = practice.sum_ints([3, -2.5, 'a', -4, 8])
    expected = 7
    n.assert_equal(result, expected, get_message(result, expected))


def test_min_and_max():
    result = practice.min_and_max([10, -5, 3, -14, 8])
    expected = (3, -14)
    n.assert_equal(result, expected, get_message(result, expected))
    result = practice.min_and_max([])
    n.assert_true(result is None, 'Need to return None of empty list.')


def test_are_palindromes():
    result = practice.are_palindromes(['abba', 'ratsliveonnoevilstar'])
    n.assert_true(result, get_message(result, True))
    result = practice.are_palindromes(['dad', 'abc'])
    n.assert_false(result, get_message(result, False))


def test_substrings():
    words = ['elephant', 'lion', 'giraffe', 'zebra']
    substrings = ['ion', 'pig', 'eta', 'raz', 'lep']
    result = practice.substring(words, substrings)
    expected = ['ion', 'lep']
    n.assert_true(isinstance(result, list), get_message(result, expected))
    n.assert_equal(set(result), set(expected), get_message(result, expected))
