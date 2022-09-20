import json
from typing import Any, Callable, Iterable, Optional


def parse_json(
    keyword_callback: Callable[[str, str], Any],
    json_str: str,
    required_fields: Optional[Iterable[str]] = None,
    keywords: Optional[Iterable[str]] = None
):
    key_filter = None
    if required_fields is not None:
        required_fields = frozenset(required_fields)

        def key_filter(kv):
            return kv[0] in required_fields

    word_filter = None
    if keywords is not None:
        keywords = frozenset(keywords)
        word_filter = keywords.__contains__

    for key, words in filter(key_filter, json.loads(json_str).items()):
        for word in filter(word_filter, words.split()):
            keyword_callback(key, word)


if __name__ == '__main__':
    def print_keyword(key, word):
        print(key, word)

    parse_json(
        print_keyword,
        json_str='{"key1": "Word1 word2", "key2": "word2 word3"}',
        required_fields=['key1'],
        keywords=['word2'],
    )
