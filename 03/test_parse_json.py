import contextlib
import json
from parse_json import parse_json


@contextlib.contextmanager
def keyword_callback():
    def callback(key, word):
        callback.keywords.append((key, word))

    callback.keywords = []
    yield callback


def test_should_filter_by_required_fields_only():
    with keyword_callback() as callback:
        parse_json(
            callback,
            json.dumps({
                'key1': 'Word1 word2',
                'key2': 'word2 Word3',
                'key3': 'word3',
            }),
            required_fields=('key3', 'key1'),
            keywords=None,
        )

        assert sorted(callback.keywords) == sorted([
            ('key1', 'Word1'),
            ('key1', 'word2'),
            ('key3', 'word3'),
        ])


def test_should_filter_by_keywords_only():
    with keyword_callback() as callback:
        parse_json(
            callback,
            json.dumps({
                'key1': 'Word1 word2',
                'key2': 'word2 Word3',
                'key3': 'word3',
            }),
            required_fields=None,
            keywords=['Word3', 'word2'],
        )

        assert sorted(callback.keywords) == sorted([
            ('key1', 'word2'),
            ('key2', 'word2'),
            ('key2', 'Word3'),
        ])


def test_should_filter_required_fields_and_keywords():
    with keyword_callback() as callback:
        parse_json(
            callback,
            json.dumps({
                'key1': 'Word1 word2',
                'key2': 'word2 word3',
            }),
            required_fields=['key1'],
            keywords=['word2'],
        )

        assert callback.keywords == [('key1', 'word2')]
