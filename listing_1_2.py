"""
Процессы и потоки в простом Python-приложении
"""
import os
import threading

print(f"Python process id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"Python running {total_threads} thread(s)")
print(f"Name of the current thread is '{thread_name}'")
