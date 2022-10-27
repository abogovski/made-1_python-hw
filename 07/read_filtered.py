import io


def __read_filtered_from_file(fileobj, target_words):
    target_words = set(word.strip().lower() for word in target_words)
    for line in fileobj:
        if set(line.lower().split()) & target_words:
            yield line.rstrip('\n')
            print('yield')


def read_filtered(f, target_words):
    if isinstance(f, str):
        with open(f) as fileobj:
            yield from __read_filtered_from_file(fileobj, target_words)

    elif isinstance(f, io.TextIOBase):
        yield from __read_filtered_from_file(f, target_words)

    else:
        raise RuntimeError(f'Unxpected type of f arg: {type(f)}')
