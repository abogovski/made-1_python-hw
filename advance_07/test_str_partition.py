def test_should_partition_by_first_occurence():
    assert 'abcdefghijkl'.partition('def') == ('abc', 'def', 'ghijkl')
    assert 'a0b0c0d0'.partition('0') == ('a', '0', 'b0c0d0')
    assert 'abcdef'.partition('0') == ('abcdef', '', '')
