from server_worker import handle_request

import argparse
import logging
import multiprocessing
import socket


_HOST = 'localhost'
_PORT = 8080


def parse_args():
    parser = argparse.ArgumentParser(description='Web document stats server')
    parser.add_argument('-k', type=int, required=True, help='Return top k most common words in response')
    parser.add_argument('-w', type=int, required=True, help='Number of server workers')
    return parser.parse_args()


def setup_logging():
    logging.basicConfig()
    logging.getLogger().setLevel('DEBUG')


def workerPool(num_workers):
    return multiprocessing.Pool(num_workers)


def inetSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def read_url(connection):
    url_len = int.from_bytes(connection.recv(2), 'big', signed=False)
    return connection.recv(url_len).decode()


def main():
    setup_logging()
    args = parse_args()

    with workerPool(args.w) as workers, inetSocket() as sckt:
        sckt.bind((_HOST, _PORT))
        sckt.listen()
        logging.info('Accepting connections')
        try:
            while True:
                connection, address = sckt.accept()
                url = read_url(connection)
                workers.apply_async(handle_request, (connection, url, args.k))
        finally:
            logging.info('Waiting for workers')
            workers.close()
            workers.join()


if __name__ == '__main__':
    main()
