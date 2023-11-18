"""
Класс потокобезопасного списка
"""
from threading import RLock
from typing import List


class IntListThreadsafe:
    def __init__(self, wrapped_list: List[int]):
        self._lock = RLock()
        self._inner_list = wrapped_list

    def __str__(self):
        return str(self._inner_list)

    def indices_of(self, to_find: int) -> List[int]:
        with self._lock:
            return [
                index
                for index, value in enumerate(self._inner_list)
                if value == to_find
            ]

    def find_and_replace(self, to_replace: int, replace_with: int) -> None:
        with self._lock:
            indices = self.indices_of(to_replace)
            for index in indices:
                self._inner_list[index] = replace_with


threadsafe_list = IntListThreadsafe([1, 2, 1, 2, 1])
threadsafe_list.find_and_replace(1, 2)

print("threadsafe_list =", threadsafe_list)
