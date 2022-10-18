import io


def __read_filtered_from_file(fileobj, target_words):
    target_words = set(word.strip().lower() for word in target_words)
    for line in fileobj:
        if set(line.lower().split()) & target_words:
            yield line.rstrip('\n')


def read_filtered(f, target_words):
    if isinstance(f, str):
        with open(f) as fileobj:
            return __read_filtered_from_file(fileobj, target_words)

    if isinstance(f, io.TextIOBase):
        return __read_filtered_from_file(f, target_words)

    raise RuntimeError(f'Unxpected type of f arg: {type(f)}')
