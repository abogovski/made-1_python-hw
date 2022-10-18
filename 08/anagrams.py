from typing import List
from collections import Counter


def __subtract(counter, c):
    counter[c] -= 1
    if not counter[c]:
        del counter[c]


def find_anagrams(text: str, pattern: str) -> List[int]:
    assert len(pattern) > 0
    result = []

    pattern_counter = Counter(pattern)
    text_counter = Counter(text[:len(pattern) - 1])

    for offset in range(len(text) - len(pattern) + 1):
        text_counter[text[offset + len(pattern) - 1]] += 1
        if offset > 0:
            __subtract(text_counter, text[offset - 1])

        if text_counter == pattern_counter:
            result.append(offset)

    return result
