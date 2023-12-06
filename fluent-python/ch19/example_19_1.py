"""
Spinner with threads
"""
import itertools
import time
from threading import Event, Thread


def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)

        if done.wait(0.2):
            break

        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


def slow() -> int:
    time.sleep(3)  # Blocks the calling thread, but releases the GIL
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=("thinking!", done))
    print(f"Spinner object: {spinner}")
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print("\rAnswer:", result)


if __name__ == "__main__":
    main()