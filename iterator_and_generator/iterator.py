"""
Realisation of the classic pattern 'Iterator'
"""

import abc
from abc import ABC


class Aggregate(ABC):

    @abc.abstractmethod
    def iterator(self):
        """Returns iterator"""
        pass


class Iterator(ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        """Return iterator to the first item
        of the iterable obj"""

    @abc.abstractmethod
    def next(self):
        """Go to the next item of the iterable"""
        pass

    @abc.abstractmethod
    def current(self):
        """Returns current item"""
        pass


class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        super().__init__(collection, cursor)

    def current(self):
        return self._collection[self._cursor]

    def first(self):
        self._cursor = -1

    def next(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1


class ListCollection(Aggregate):

    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)


if __name__ == '__main__':
    collection = (1, 2, 3, 4, 5)
    aggregate = ListCollection(collection)
    itr = aggregate.iterator()
    while True:
        try:
            itr.next()
        except StopIteration:
            break
        print(itr.current())
