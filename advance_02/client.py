import argparse
import json
import logging
import multiprocessing
import socket


_HOST = 'localhost'
_PORT = 8080
_LOCK = multiprocessing.Lock()


def setup_logging():
    logging.basicConfig()
    logging.getLogger().setLevel('DEBUG')


def parse_args():
    parser = argparse.ArgumentParser('Web document stats client')
    parser.add_argument('num_workers', type=int)
    parser.add_argument('urls')
    return parser.parse_args()


def workerPool(num_workers):
    return multiprocessing.Pool(num_workers)


def inetSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def write_url(sckt, url):
    sckt.sendall(len(url).to_bytes(2, 'big', signed=False) + url.encode())


def read_json(sckt):
    json_len = int.from_bytes(sckt.recv(2), 'big', signed=False)
    return json.loads(sckt.recv(json_len).decode())


def make_request(url):
    try:
        with inetSocket() as sckt:
            sckt.connect((_HOST, _PORT))
            write_url(sckt, url)
            response = read_json(sckt)

        with _LOCK:
            print(response)
    except Exception as ex:
        logging.error(str(ex))


def main():
    setup_logging()
    args = parse_args()

    with workerPool(args.num_workers) as workers, open(args.urls) as f:
        for line in f:
            workers.apply_async(make_request, (line.strip(),))
        workers.close()
        workers.join()


if __name__ == '__main__':
    main()
