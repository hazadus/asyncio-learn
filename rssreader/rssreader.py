import asyncio
import feedparser
import logging

from aiohttp import ClientSession
from util import async_timed

FEED_URLS = [
    "https://hazadus.ru/rss.xml",
    "http://adamj.eu/tech/atom.xml",
    "https://antfu.me/feed.xml",
    "https://www.bencodezen.io/rss.xml",
    "https://www.better-simple.com/atom.xml",
    "https://brntn.me/rss/",
    "https://css-tricks.com/feed/",
    "https://daniel.feldroy.com/feeds/atom.xml",
    "https://www.digitalocean.com/community/articles/feed.atom",
    "https://www.freecodecamp.org/news/rss/",
    "https://joshcollinsworth.com/api/rss.xml",
    "https://www.joshwcomeau.com/rss.xml",
    "https://martinfowler.com/feed.atom",
    "https://mokkapps.de/rss.xml",
    "https://quickwit.io/blog/rss.xml",
    "https://realpython.com/atom.xml",
    "https://www.stefanjudis.com/rss.xml",
    "http://www.snarky.ca/feed",
    "http://testdriven.io/feed.xml",
    "https://github.com/blog/all.atom",
    "https://github.com/readme.rss",
    "https://this-week-in-rust.org/rss.xml",
    "http://blog.wesleyac.com/feed.xml",
    "http://www.residentadvisor.net/xml/review-album.xml",
    "http://www.residentadvisor.net/xml/features.xml",
    "http://www.residentadvisor.net/xml/review-single.xml",
    "https://teletype.in/rss/temalebedev",
    "https://autoreview.ru/feed/news/rss",
    "http://www.3dnews.ru/news/main/rss",
    "http://www.3dnews.ru/video/rss/",
    "http://www.3dnews.ru/cooling/rss/",
    "http://www.3dnews.ru/display/rss/",
    "http://www.3dnews.ru/mobile/rss/",
    "http://www.3dnews.ru/smart-things/rss/",
    "https://www.mirf.ru/feed",
    "http://stopgame.ru/rss/rss_news.xml",
    "http://stopgame.ru/rss/rss_review.xml",
    "http://stopgame.ru/rss/rss_preview.xml",
    "https://dtf.ru/rss/all",
    "http://feeds.feedburner.com/RockPaperShotgun",
    "http://igromania.ru/rss/rss_articles.xml",
    "http://torick.ru/feed/",
    "http://feeds.howtogeek.com/HowToGeek",
    "https://www.macworld.com/feed",
    "https://surface-pro.ru/feed/",
    "http://disgustingmen.com/feed/",
    "https://blog.rabbitmq.com/index.xml",
    "https://wsvincent.com/feed.xml",
    "https://blog.miguelgrinberg.com/feed",
    "https://www.djangoproject.com/rss/weblog/",
    "https://django-news.com/issues.rss",
    "http://tonsky.me/blog/atom.xml",
    "https://www.blog.pythonlibrary.org/feed/",
    "https://pxlnv.com/feed",
    "https://thesweetsetup.com/feed",
    "https://www.macstories.net/feed/",
    "https://inessential.com/xml/rss.xml",
    "https://jacobian.org/feed/",
]


async def fetch_feed(session: ClientSession, url: str):
    async with session.get(url) as response:
        return await response.text()


async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_feed(session, url=url)) for url in FEED_URLS
        ]

        # Fetch all feeds - repeat until all tasks are complete
        htmls = []
        while pending:
            # Return from `wait` on first completed task:
            done, pending = await asyncio.wait(
                pending, return_when=asyncio.FIRST_COMPLETED
            )

            print(f"Done tasks...: {len(done)}")
            print(f"Pending tasks: {len(pending)}")

            for done_task in done:
                if done_task.exception() is None:
                    html = done_task.result()
                    print(f"{html[:100]=}...")
                    htmls.append(html)
                else:
                    logging.error(
                        "An error has occured during request",
                        exc_info=done_task.exception(),
                    )

        # Parse all fetched feeds
        print(f"{len(htmls)=}")
        parsed_feeds = [feedparser.parse(html) for html in htmls]
        print(f"{len(parsed_feeds)=}")

        # Get all entry URLs from all feeds
        entry_urls = []
        for feed in parsed_feeds:
            for item in feed.get("items"):
                entry_urls.append(item.get("link", None))
        print(f"{len(entry_urls)=}")

        # Get status code for each entry URL
        pending = [
            asyncio.create_task(fetch_status(session, url=url))
            for url in entry_urls
            if url is not None
        ]

        # Repeat until all tasks are complete
        while pending:
            # Return from `wait` on first completed task:
            done, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED,
                timeout=5,
            )

            print(f"Done tasks...: {len(done)}")
            print(f"Pending tasks: {len(pending)}")

            for done_task in done:
                if done_task.exception() is None:
                    print(f"{done_task.result()=}")
                else:
                    logging.error(
                        "An error has occured during request",
                        exc_info=done_task.exception(),
                    )


asyncio.run(main())
