"""
That are the disadvantages here?
The huge problem is that the mapreduce() function is not generic at all.
If you want write another subclass of InputData or Worker then you will
also rewrite generate_inputs(), create_workers() and mapreduce() functions."""
import os
from threading import Thread


class InputData:
    """Generic class for representing
    input data"""

    def read(self):
        raise NotImplementedError


class Worker:
    """Generic class for work bringing
    the MapReduce node"""

    def __init__(self, input_data: InputData):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class PathInputData(InputData):
    """Read data from file"""

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class LineCounterWorker(Worker):
    """Line counter worker"""

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCounterWorker(input_data))
    return workers


def execute(workers: list[Worker]):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)

    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)
