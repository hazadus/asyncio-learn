"""
http://localhost:8000/requests/?url=https://hazadus.ru&request_num=100
"""
import asyncio
from datetime import datetime

import aiohttp
from aiohttp import ClientSession
from django.shortcuts import render


async def get_url_details(session: ClientSession, url: str):
    start_time = datetime.now()
    response = await session.get(url)
    response_body = await response.text()
    end_time = datetime.now()
    return {
        "status": response.status,
        "time": (end_time - start_time).microseconds,
        "body_length": len(response_body),
    }


async def make_requests(url: str, request_num: int):
    async with aiohttp.ClientSession() as session:
        requests = [get_url_details(session, url) for _ in range(request_num)]
        results = await asyncio.gather(*requests, return_exceptions=True)
        failed_results = [
            str(result) for result in results if isinstance(result, Exception)
        ]
        successful_results = [
            result for result in results if not isinstance(result, Exception)
        ]
        return {
            "failed_results": failed_results,
            "successful_results": successful_results,
        }


async def requests_view(request):
    url: str = request.GET["url"]
    request_num: int = int(request.GET["request_num"])
    context = await make_requests(url, request_num)
    return render(request, "async_api/requests.html", context)
