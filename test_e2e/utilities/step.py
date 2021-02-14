import functools


def step(to_print):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            STEP_IN(to_print)
            return func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat


def STEP_IN(to_print):
    print(str(to_print))


def SCENARIO_IN(to_print):
    print("")
    print("Scenario name : "+str(to_print))


def scenario(to_print):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            SCENARIO_IN(to_print)
            return func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat
