"""
Простое ASGI-приложение

Runnning the app:
uvicorn ch9.listing_9_7:application
"""


async def application(scope, receive, send):
    for key in scope.keys():
        print(f"'{key}': '{scope[key]}'")

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/html"]],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Hello ASGI world!",
        }
    )
