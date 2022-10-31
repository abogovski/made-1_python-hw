from abc import ABC, abstractmethod
import csv
import json


class BaseReader(ABC):
    @abstractmethod
    def load():
        pass


class BaseWriter(ABC):
    @abstractmethod
    def dump():
        pass


class TxtReader(BaseReader):
    def load(self, fileobj):
        return [
            s.rstrip('\n').encode().decode('unicode_escape')
            for s in fileobj
        ]


class TxtWriter(BaseWriter):
    def dump(self, data, fileobj):
        for s in data:
            fileobj.write(s.encode('unicode_escape').decode() + '\n')


class JsonReader(BaseReader):
    def load(self, fileobj):
        return json.load(fileobj)


class JsonWriter(BaseWriter):
    def dump(self, data, fileobj):
        json.dump(data, fileobj)


class CsvReader(BaseReader):
    def load(self, fileobj):
        return list(csv.reader(fileobj))


class CsvWriter(BaseWriter):
    def dump(self, data, fileobj):
        writer = csv.writer(fileobj)
        for row in data:
            writer.writerow(row)


def read_data(fileobj, reader: BaseReader):
    return reader.load(fileobj)


def dump_data(data, fileobj, writer: BaseWriter):
    writer.dump(data, fileobj)
