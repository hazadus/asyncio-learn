"""
Web crawler built with asyncio.
Scrapes unique URLs from web pages to the desired depth, and saves it to a file.
"""
import asyncio
import os
from asyncio import Lock, Queue
from http import HTTPStatus
from time import perf_counter

from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientConnectorError, ClientResponseError
from bs4 import BeautifulSoup

START_URL = "https://amgold.ru"
OUTPUT_PATH = "./links.txt"
MAX_DEPTH = 3
MAX_CRAWLERS = 32
MAX_TIMEOUT = 2.0


class Page:
    def __init__(self, url: str, level: int = 1):
        self._url = url
        self._level = level

    @property
    def url(self):
        return self._url

    @property
    def level(self):
        return self._level


async def crawl_worker(queue: Queue, crawler_id: int, result_set: set[str], lock: Lock):
    # Пауза для предотвращения остановки, пока в очереди еще мало объектов для обработки
    if crawler_id > 0:
        timeout = 2 if crawler_id < 3 else 0.5
        await asyncio.sleep(timeout)

    while not queue.empty():
        page: Page = queue.get_nowait()
        print(f">> W {crawler_id:2d} LVL {page.level} URL {page.url} ...")

        try:
            async with ClientSession(
                timeout=ClientTimeout(total=MAX_TIMEOUT)
            ) as session:
                async with session.get(page.url) as response:
                    if response.status != HTTPStatus.OK:
                        return

                    content: bytes = await response.content.read()
                    urls = get_all_urls(content)

                    added_urls_count = 0

                    for url in urls:
                        async with lock:
                            if url not in result_set:
                                added_urls_count += 1
                                result_set.add(url)
                                if page.level < MAX_DEPTH:
                                    queue.put_nowait(
                                        Page(url=url, level=page.level + 1)
                                    )
                    print(
                        f"<< W {crawler_id:2d} LVL {page.level} FOUND {len(urls):3d}, NEW {added_urls_count:3d} "
                        f"TOTAL {len(result_set):5d} in URL {page.url}"
                    )
        except ClientConnectorError as ex:
            print("Error connecting to", page.url)
        except asyncio.exceptions.TimeoutError as ex:
            print("Connection timed out:", page.url)
        except ClientResponseError as ex:
            print("Error decoding content:", page.url)

        queue.task_done()


def get_all_urls(content: bytes) -> set:
    """Return set of unique external URLs found in `content`."""
    soup = BeautifulSoup(content, "html.parser")

    urls = set()
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            urls.add(href)

    return urls


def save_to_file(result: set[str], output_path: str):
    if os.path.exists(output_path):
        os.remove(output_path)

    with open(output_path, mode="w") as file:
        for line in result:
            file.write(f"{line}\n")


async def main():
    crawl_queue = Queue()

    all_pages = [
        Page(url=START_URL),
    ]

    [crawl_queue.put_nowait(page) for page in all_pages]

    result_set = {START_URL}  # Create output set with initial URL included
    lock = Lock()
    crawlers = [
        asyncio.create_task(crawl_worker(crawl_queue, crawler_id, result_set, lock))
        for crawler_id in range(MAX_CRAWLERS)
    ]

    start = perf_counter()
    await asyncio.gather(
        crawl_queue.join(),
        *crawlers,
    )
    save_to_file(result_set, OUTPUT_PATH)

    elapsed = perf_counter() - start
    print(f"Crawling complete. Found {len(result_set)} unique URLs in {elapsed:.2f} s.")


if __name__ == "__main__":
    asyncio.run(main())
