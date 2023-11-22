"""
WSGI-приложение

Runnning the app:
gunicorn ch9.listing_9_6
"""


def application(env, start_response):
    print(f"{start_response=}")

    for key in env.keys():
        print(f"'{key}': '{env[key]}'")

    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Hello WSGI world!"]
