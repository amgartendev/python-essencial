from functools import wraps
from datetime import datetime


def log(func):
    """Create a log file with the values and the function called in a new log.txt file"""
    @wraps(func)
    def logging(*args, **kwargs):
        with open('logs.txt', 'a') as file:
            file.write(f'Called a function named {func.__name__} with {[" ".join([str(arg) for arg in args])]} at {str(datetime.now())}\n')
        value = func(*args, **kwargs)
        return value
    return logging


@log
def run_gabriel(a, b, c=9):
    """Gabriel's function"""
    return f'Values used: {a} {b} {c}'


@log
def run_joao(a, b, c=9):
    """João's function"""
    return f'Values used: {a} {b} {c}'


run_gabriel(1, 2, 3)
run_joao(5, 2, 7)


print(run_gabriel.__name__)
print(run_gabriel.__doc__)
