"""
Download random cat photos using sequential downloads vs. threading vs. multiprocessing modules.
"""
import logging
import multiprocessing
import os
import threading
import time
import uuid
from http import HTTPStatus

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAT_URL = "https://cataas.com/cat"
OUT_DIR = "./cats"
OUT_PATH = "cats/{}.jpeg"
CATS_QTY = 10

filename = uuid.uuid4()


def download_image(url: str, output_path: str):
    response = requests.get(url, timeout=(5, 5))

    if response.status_code != HTTPStatus.OK:
        return

    with open(output_path, "wb") as file:
        file.write(response.content)


def load_images_sequential():
    start = time.time()

    for i in range(CATS_QTY):
        download_image(CAT_URL, OUT_PATH.format(uuid.uuid4()))
        logger.info("Downloaded cat #%d", i + 1)

    logger.info(
        "Downloaded {qty} cats sequentially in {sec:.2f} sec.".format(
            qty=CATS_QTY, sec=time.time() - start
        )
    )


def load_images_multithreaded():
    start = time.time()

    threads = []
    for i in range(CATS_QTY):
        thread = threading.Thread(
            target=download_image,
            args=(
                CAT_URL,
                OUT_PATH.format(uuid.uuid4()),
            ),
        )
        thread.start()
        threads.append(thread)

    [thread.join() for thread in threads]

    logger.info(
        "Downloaded {cat_qty} cats using {thread_qty} threads in {sec:.2f} sec.".format(
            cat_qty=CATS_QTY,
            thread_qty=CATS_QTY,
            sec=time.time() - start,
        )
    )


def load_images_multiprocessing():
    start = time.time()

    processes = []
    for i in range(CATS_QTY):
        process = multiprocessing.Process(
            target=download_image,
            args=(
                CAT_URL,
                OUT_PATH.format(uuid.uuid4()),
            ),
        )
        process.start()
        processes.append(process)

    [process.join() for process in processes]

    logger.info(
        "Downloaded {cat_qty} cats using {process_qty} processes in {sec:.2f} sec.".format(
            cat_qty=CATS_QTY,
            process_qty=CATS_QTY,
            sec=time.time() - start,
        )
    )


if __name__ == "__main__":
    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)

    logger.info(f"Starting sequential download of {CATS_QTY} cats...")
    load_images_sequential()

    logger.info(f"Starting multithreaded download of {CATS_QTY} cats...")
    load_images_multithreaded()

    logger.info(f"Starting multiprocess download of {CATS_QTY} cats...")
    load_images_multiprocessing()
