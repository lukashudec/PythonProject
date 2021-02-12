import functools


def step(to_print):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            step_in(to_print)
            return func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat


def step_in(to_print):
    print(str(to_print))
