from read_filtered import read_filtered
from io import StringIO


def test_read_filtered():
    result = read_filtered(
        StringIO(
            'wOrd1 word2\n'
            'word2 word4 word6\n'
            '\n'
            'word3   \n'
        ),
        ['word1', 'wOrd3'],
    )

    assert list(result) == [
        'wOrd1 word2',
        'word3   '
    ]
