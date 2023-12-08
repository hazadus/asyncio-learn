"""
Dining philosophers.
https://go.skillbox.ru/profession/profession-python/python-advanced/2f69f1b7-202f-49a3-b020-a734f24dbcda/videolesson
"""
import logging
import random
import threading
import time

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    is_running = True

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.is_running:
            logger.info(f"Philosopher {self.name} start thinking.")
            time.sleep(random.randint(1, 5))
            logger.info(f"Philosopher {self.name} is hungry.")

            try:
                self.left_fork.acquire()
                time.sleep(random.randint(1, 5))
                logger.info(f"Philosopher {self.name} acquired left fork.")

                if self.right_fork.locked():
                    continue

                try:
                    self.right_fork.acquire()
                    logger.info(f"Philosopher {self.name} acquired right fork.")
                    self.dining()
                finally:
                    self.left_fork.release()
                    self.right_fork.release()
            finally:
                if self.left_fork.locked():
                    self.left_fork.release()

    def dining(self):
        logger.info(f"Philosopher {self.name} started eating.")
        time.sleep(random.randint(1, 5))
        logger.info(f"Philosopher {self.name} finished eating.")


def main():
    forks = [threading.Lock() for n in range(5)]
    philosophers = [
        Philosopher(
            forks[i % 5],
            forks[(i + 1) % 5],
        )
        for i in range(5)
    ]

    Philosopher.is_running = True
    [phil.start() for phil in philosophers]
    time.sleep(200)
    Philosopher.is_running = False
    logger.info("Now we are done.")


if __name__ == "__main__":
    main()
