import pytest
import serialization as s
from copy import deepcopy
from io import StringIO


@pytest.mark.parametrize('base', [s.BaseReader, s.BaseWriter])
def test_base_classes_are_abstract(base):
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        base()


@pytest.mark.parametrize('reader', [s.TxtReader, s.CsvReader, s.JsonReader])
def test_readers_should_be_derived_from_base_reader(reader):
    assert issubclass(reader, s.BaseReader)


@pytest.mark.parametrize('writer', [s.TxtWriter, s.CsvWriter, s.JsonWriter])
def test_writers_should_be_derived_from_base_writer(writer):
    assert issubclass(writer, s.BaseWriter)


@pytest.mark.parametrize(
    'reader,writer,data',
    [
        (s.TxtReader, s.TxtWriter, ['']),
        (s.CsvReader, s.CsvWriter, [[]]),
        (s.JsonReader, s.JsonWriter, None),
        (s.JsonReader, s.JsonWriter, []),
        (s.JsonReader, s.JsonWriter, {}),

        (s.TxtReader, s.TxtWriter, ['a b', '', '\n']),
        (s.CsvReader, s.CsvWriter, [['a,b', 'c d'], ['1 2', '3\n4']]),
        (s.JsonReader, s.JsonWriter, {'k': [0, 1, 2, 3]}),
    ]
)
def test_load_dump(reader, writer, data):
    fileobj = StringIO()
    s.dump_data(deepcopy(data), fileobj, writer())
    fileobj.seek(0)
    assert s.read_data(fileobj, reader()) == data
