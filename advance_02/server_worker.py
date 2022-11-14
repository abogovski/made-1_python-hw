import chardet
import json
import logging
import multiprocessing
import re

from collections import Counter
from urllib3.util import parse_url
from urllib3 import PoolManager


_RE_ALPHANUM = re.compile(r'\w+', re.MULTILINE)
_COUNTER = multiprocessing.Value('i', 0)
_HTTP = PoolManager()


def _ensure_https_url(url):
    return parse_url(url)._replace(scheme='https').url


def _ensure_str(data):
    if isinstance(data, str):
        logging.debug('Data has been already decoded by urllib3')
        return data

    assert isinstance(data, bytes), f'Unexpected data type {type(data)}'
    encoding = chardet.detect(data)
    logging.debug(f'Detected encoding {encoding}')
    return data.decode(encoding=encoding['encoding'])


def _fetch_data(http, url):
    data = http.request('GET', url, preload_content=True, decode_content=True).data
    return data


def _top_word_count(text, num_top):
    logging.debug(f'Collecting {num_top} most common words')
    words = map(lambda match: match.group(0).lower(), re.finditer(_RE_ALPHANUM, text))
    return dict(Counter(words).most_common(num_top))


def _write_json(connection, obj):
    serialized = json.dumps(obj).encode()
    connection.sendall(len(serialized).to_bytes(2, 'big', signed=False) + serialized)


def handle_request(connection, url, num_top):
    try:
        logging.info(f'Handling url={url} num_top={num_top} request')
        data = _fetch_data(_HTTP, _ensure_https_url(url))
        top_wc = _top_word_count(_ensure_str(data), num_top)
        _write_json(connection, top_wc)

    except Exception as ex:
        logging.error(f'Url fetch {url} failed with {ex}')
        _write_json(connection, {'$error': str(ex)})

    finally:
        with _COUNTER.get_lock():
            _COUNTER.value += 1
            logging.info(f'Now processed {_COUNTER.value} requests')
        connection.close()
