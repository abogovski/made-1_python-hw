import pytest
from copy import deepcopy
from io import StringIO
from serialization import *


def test_base_classes_are_abstract():
    for base_class in (BaseReader, BaseWriter):
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            base_class()


def test_readers_should_be_derived_from_base_reader():
    for reader in (TxtReader, CsvReader, JsonReader):
        assert issubclass(reader, BaseReader)


def test_writers_should_be_derived_from_base_writer():
    for writer in (TxtWriter, CsvWriter, JsonWriter):
        assert issubclass(writer, BaseWriter)


@pytest.mark.parametrize(
    'reader,writer,data',
    [
        (TxtReader, TxtWriter, ['']),
        (CsvReader, CsvWriter, [[]]),
        (JsonReader, JsonWriter, None),
        (JsonReader, JsonWriter, []),
        (JsonReader, JsonWriter, {}),

        (TxtReader, TxtWriter, ['a b', '', '\n']),
        (CsvReader, CsvWriter, [['a b', 'c,d', 'e f'], ['1 2', '3 4', '5\n6']]),
        (JsonReader, JsonWriter, {'k': [0, 1, 2, 3]}),
    ]
)
def test_load_dump(reader, writer, data):
    fileobj = StringIO()
    dump_data(deepcopy(data), fileobj, writer())
    fileobj.seek(0)
    assert read_data(fileobj, reader()) == data
