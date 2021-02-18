import functools
import time

from locust import events


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
    print("Scenario name : " + str(to_print))


def measured_step(name):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            start_time = time.time()
            ret = func(*args, **kwargs)
            stop_time = (time.time() - start_time) * 1000
            STEP_IN(name)
            events.request_success.fire(request_type="measure",
                                        name=name,
                                        response_time=int(stop_time),
                                        response_length=10)
            return ret

        return wrapper_repeat

    return decorator_repeat


def scenario(to_print):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            SCENARIO_IN(to_print)
            return func(*args, **kwargs)

        return wrapper_repeat

    return decorator_repeat
