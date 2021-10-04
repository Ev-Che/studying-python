import collections
from typing import Iterator


class ListIterator(collections.abc.Iterator):
    def __init__(self, collection, cursor):
        self._cursor = cursor
        self._collection = collection

    def __next__(self):
        self._cursor += 1

        if self._cursor >= len(self._collection):
            raise StopIteration
        return self._collection[self._cursor]


class ListCollection(collections.abc.Iterable):

    def __init__(self, user_collection):
        self._collection = user_collection

    def __iter__(self) -> Iterator:
        return ListIterator(self._collection, -1)


if __name__ == '__main__':
    collection = (1, 2, 3, 4, 5)
    aggregate = ListCollection(collection)
    for item in aggregate:
        print(item)

    for item in aggregate:
        print(item)
