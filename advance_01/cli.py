import argparse
import logging
import sys
from lru_cache import LRUCache


def parse_args():
    parser = argparse.ArgumentParser(description='CLI to play with LRUCache')
    parser.add_argument('-n', help='Cache size. Defaults to 5.', default=5)
    parser.add_argument('-s', help='Duplicate log output to stdout', action='store_true')
    return parser.parse_args()


def create_log_file_handler():
    handler = logging.FileHandler('./cache.log')
    handler.setFormatter(
        logging.Formatter('%(levelname)s %(asctime)s %(message)s')
    )
    return handler


def create_log_stdout_handler():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter('[%(levelname)s] %(funcName)s @ %(msecs)dms: %(message)s')
    )
    return handler


def setup_logging(duplicate_to_stdout):
    handlers = [create_log_file_handler()]
    if duplicate_to_stdout:
        handlers.append(create_log_stdout_handler())

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=handlers
    )


def exec_cache_command(cache, command):
    words = command.split()
    if words[0] == 'set':
        cache.set(*words[1:])
    elif words[0] == 'get':
        print(cache.get(*words[1]) or 'null')
    else:
        raise RuntimeError(f'Unexpected command {words[0]}')


def main():
    args = parse_args()
    setup_logging(args.s)

    cache = LRUCache(args.n)
    for i, line in enumerate(sys.stdin):
        try:
            exec_cache_command(cache, line)
        except Exception as ex:
            logging.error(
                'Got exception "%s" when executing "%s" at line %d',
                ex, line.strip(), i + 1
            )
            logging.info('Ignoring unexpected error')


if __name__ == '__main__':
    main()
