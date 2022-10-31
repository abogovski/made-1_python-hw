import json
from typing import Any, Callable, Iterable, Optional


def parse_json(
    keyword_callback: Callable[[str, str], Any],
    json_str: str,
    required_fields: Optional[Iterable[str]] = None,
    keywords: Optional[Iterable[str]] = None
):
    '''
    Expects jsonized dict[str, str]. For each `field` and each `word`
    in respective value calls `keyword_callback(field, word)`.

    Filters `(field, word)` pairs by `field` presence in `required_fields`,
    if iterable `required_fields` is specified.

    Filters `(field, word)` pairs by `word` presence in `keywords`,
    if iterable `keywords` is specified.
    '''
    field_filter = None
    if required_fields is not None:
        required_fields = frozenset(required_fields)

        def field_filter(kv):
            return kv[0] in required_fields

    word_filter = None
    if keywords is not None:
        keywords = frozenset(keywords)
        word_filter = keywords.__contains__

    for field, words in filter(field_filter, json.loads(json_str).items()):
        for word in filter(word_filter, words.split()):
            keyword_callback(field, word)
