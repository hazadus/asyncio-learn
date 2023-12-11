import asyncio
import socket
from keyword import kwlist

DOMAINS = ["dev", "io"]


async def probe(site_domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()

    try:
        # This will succeed if `site_domain` exists:
        await loop.getaddrinfo(site_domain, None)
    except socket.gaierror:
        return site_domain, False
    return site_domain, True


async def main() -> None:
    # Use Cartesian product to create generator of all combinations of Python
    # keywords and our preferred domains:
    site_domains = (f"{kw}.{domain}" for kw in kwlist for domain in DOMAINS)
    coros = [probe(site_domain) for site_domain in site_domains]
    for coro in asyncio.as_completed(coros):
        domain, is_found = await coro
        mark = "+" if is_found else " "
        print(f"{mark} {domain}")


if __name__ == "__main__":
    asyncio.run(main())
