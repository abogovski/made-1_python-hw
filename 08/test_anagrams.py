from anagrams import find_anagrams


def test_find_anagrams():
    assert find_anagrams('abcba', 'abc') == [0, 2]
    assert find_anagrams('aaa', 'a') == [0, 1, 2]
    assert find_anagrams('abc cba xabcd', 'abc') == [0, 4, 9]
