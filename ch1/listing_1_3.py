"""
Создание многопоточного Python-приложения
"""
import threading


def hello_from_thread():
    print(f"Hello from thread {threading.current_thread()}")


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"Python is currently running {total_threads} thread(s)")
print(f"Current thread name is '{thread_name}'")

# Wait until the thread is completed
hello_thread.join()
