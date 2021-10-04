"""
Fibonacci sequence generator
"""


class FibonacciGenerator:
    def __init__(self):
        self._prev = 0
        self._current = 1

    def get_fibonacci(self):
        while True:
            yield self._prev
            self._prev, self._current = (self._current,
                                         self._current + self._prev)


if __name__ == '__main__':
    gen = FibonacciGenerator().get_fibonacci()
    fibonacci_item = 0

    while fibonacci_item < 100:
        fibonacci_item = next(gen)
        print(fibonacci_item)

    # for item in gen:
    #     print(item)
