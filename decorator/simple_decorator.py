# If realize decorator without @wraps(func):
#   When func decorated: foo = decorator(foo)
#   And if __name__ called: foo.__name__ == wrap
# If realize decorator WITH @wraps(func)
#   And call __name__: foo.__name__ == foo

from functools import wraps


def decorator_with_args(message):

    print(f'decorator arg: {message}')

    def decorator(decorated_func):
        print(f'decorator arg: {message} inside decorator')

        @wraps(decorated_func)
        def wrap(*args, **kwargs):
            print(f'decorator arg: {message} inside wraps')
            print(f'Actions before {decorated_func.__name__} called')
            result = decorated_func(*args, **kwargs)
            print(f'Actions after {decorated_func.__name__} called')
            return result

        return wrap

    return decorator


@decorator_with_args('message')
def foo(a, b):
    print('function starts')
    result = a / b
    print('function ends')
    return result


if __name__ == '__main__':
    print(foo(5, 5))
    print(foo.__name__)
    print('*' * 10)
    print(foo(5, 5))
