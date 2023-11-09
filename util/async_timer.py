import functools
import time
from typing import Callable, Any


def async_timed():
    """
    Декоратор для хронометража сопрограмм
    """

    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Calling {func} with arguments {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{func} completed in {total:.4f} sec.")

        return wrapped

    return wrapper
