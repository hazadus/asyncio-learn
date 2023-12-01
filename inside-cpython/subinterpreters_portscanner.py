"""
Сканер портов с использованием `subinterpreters`
"""
import textwrap
import time
from queue import Queue
from threading import Thread

import _xxsubinterpreters as subinterpreters

TIMEOUT = 1  # sec


def run(host: str, port: int, results: Queue):
    channel_id = subinterpreters.channel_create()
    interpid = subinterpreters.create()
    subinterpreters.run_string(
        interpid,
        textwrap.dedent(
            """
            import socket
            import _xxsubinterpreters as subinterpreters
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            subinterpreters.channel_send(channel_id, result)
            sock.close()
            """
        ),
        shared=dict(
            channel_id=channel_id,
            host=host,
            port=port,
            timeout=TIMEOUT,
        ),
    )
    output = subinterpreters.channel_recv(channel_id)
    subinterpreters.channel_release(channel_id)

    if output == 0:
        results.put(port)


if __name__ == "__main__":
    start = time.time()
    host = "127.0.0.1"
    threads = []
    results = Queue()

    for port in range(80, 100):
        t = Thread(target=run, args=(host, port, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    while not results.empty():
        print(f"Port {results.get()} is open.")

    print(f"Scan completed in {time.time() - start} sec.")
