"""
Requesting web API using ThreadPoolExecutor and ProcessPoolExecutor, featuring:
- using `concurrent.futures.as_completed()`;
- proper exception handling for each thread or process using future mapping.
"""
import logging
import os
import sqlite3
from concurrent.futures import (
    Future,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
)
from dataclasses import dataclass
from time import perf_counter

import requests

DATABASE_FILENAME = "sw_database.db"


class CharacterNotFound(Exception):
    pass


class APIRequestError(Exception):
    pass


@dataclass
class Character:
    name: str
    gender: str
    birth_year: str


def get_character(character_id: int) -> Character:
    url = f"https://swapi.dev/api/people/{character_id}/"

    try:
        response = requests.get(url)
    except Exception as ex:
        raise APIRequestError

    json = response.json()

    if json.get("detail") == "Not found":
        raise CharacterNotFound

    return Character(
        name=json.get("name"),
        gender=json.get("gender"),
        birth_year=json.get("birth_year"),
    )


def get_characters_using_threadpoolexecutor() -> list[Character]:
    start = perf_counter()
    results: list[Character] = []

    logger.info("Download using ThreadPoolExecutor started.")

    with ThreadPoolExecutor(max_workers=10) as executor:
        tasks: list[Future] = []
        future_to_id: dict[Future, int] = {}

        for character_id in range(1, 22):
            future = executor.submit(get_character, character_id)
            tasks.append(future)
            future_to_id[future] = character_id
            logger.info("Scheduled for characted_id=%d: %s", character_id, future)

        for future in as_completed(tasks):
            try:
                res: Character = future.result()
                logger.info("%s result: %s", future, res)
                results.append(res)
            except Exception as ex:
                logger.exception(
                    "An error has occured while trying to get characted_id=%d",
                    future_to_id[future],
                    exc_info=ex,
                )

    logger.info(
        f"Download using ThreadPoolExecutor completed in {perf_counter()-start:.2f} sec."
    )
    return list(results)


def get_characters_using_processpoolexecutor() -> list[Character]:
    start = perf_counter()
    results: list[Character] = []

    logger.info("Download using ProcessPoolExecutor started.")

    with ProcessPoolExecutor() as executor:
        tasks: list[Future] = []
        future_to_id: dict[Future, int] = {}

        for character_id in range(22, 42):
            future = executor.submit(get_character, character_id)
            tasks.append(future)
            future_to_id[future] = character_id
            logger.info("Scheduled for characted_id=%d: %s", character_id, future)

        for future in as_completed(tasks):
            try:
                res: Character = future.result()
                logger.info("%s result: %s", future, res)
                results.append(res)
            except Exception as ex:
                logger.exception(
                    "An error has occured while trying to get characted_id=%d",
                    future_to_id[future],
                    exc_info=ex,
                )

    logger.info(
        f"Download using ProcessPoolExecutor completed in {perf_counter()-start:.2f} sec."
    )
    return list(results)


def reset_database() -> None:
    if os.path.exists(DATABASE_FILENAME):
        os.remove(DATABASE_FILENAME)

    with sqlite3.connect(DATABASE_FILENAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE characters (
                id integer PRIMARY KEY,
                name text,
                gender text,
                birth_year text
            );
            """
        )


def add_characters_to_database(characters: list[Character]) -> None:
    with sqlite3.connect(DATABASE_FILENAME) as conn:
        cursor = conn.cursor()
        cursor.executemany(
            """
            INSERT INTO characters(name, gender, birth_year)
            VALUES ($1, $2, $3)
            """,
            [(ch.name, ch.gender, ch.birth_year) for ch in characters],
        )


logging.basicConfig(
    level="INFO",
    format="%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting the application.")

    total_characters: list[Character] = []
    chars = get_characters_using_threadpoolexecutor()
    logger.info(
        "Retrieved data for %d characters using ThreadPoolExecutor.", len(chars)
    )
    total_characters.extend(chars)

    chars = get_characters_using_processpoolexecutor()
    logger.info(
        "Retrieved data for %d characters using ProcessPoolExecutor.", len(chars)
    )
    total_characters.extend(chars)

    logger.info(
        "Saving %d characters to '%s'...", len(total_characters), DATABASE_FILENAME
    )
    reset_database()
    add_characters_to_database(total_characters)
