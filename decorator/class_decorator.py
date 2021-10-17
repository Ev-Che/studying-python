from functools import wraps


class DecoratorWithoutArgs:
    def __init__(self, func):
        self.decorated_func = func

    def __call__(self, *args, **kwargs):
        print(f'Actions before {self.decorated_func.__name__} called')
        result = self.decorated_func(*args, **kwargs)
        print(f'Actions after {self.decorated_func.__name__} called')
        return result


class DecoratorWithArgs:
    def __init__(self, message):
        self.message = message

    def __call__(self, decorated_func):

        @wraps(decorated_func)
        def wrap(*args, **kwargs):
            print(f'Decorator args: {self.message}')
            print(f'Decorated func {decorated_func.__name__} called')
            return decorated_func(*args, **kwargs)
        return wrap


# @DecoratorWithArgs('message')
@DecoratorWithoutArgs
def foo(a, b):
    print('function starts')
    result = a / b
    print('function ends')
    return result


if __name__ == '__main__':
    print(foo(5, 5))
