"""
Access web API using process pool vs. thread pool.
"""
import logging
import multiprocessing
import os
import sqlite3
from dataclasses import dataclass
from multiprocessing.pool import ThreadPool
from time import perf_counter

import requests

DATABASE_FILENAME = "sw_database.db"

logging.basicConfig(
    level="INFO",
    format="%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


@dataclass
class Character:
    name: str
    gender: str
    birth_year: str


def get_character(character_id: int) -> Character | None:
    url = f"https://swapi.dev/api/people/{character_id}/"

    try:
        response = requests.get(url)
    except Exception:
        return None

    try:
        json = response.json()
    except Exception:
        return None

    if json.get("detail") == "Not found":
        return None

    return Character(
        name=json.get("name"),
        gender=json.get("gender"),
        birth_year=json.get("birth_year"),
    )


def get_characters_using_process_pool() -> list[Character]:
    start = perf_counter()
    results: list[Character] = []

    logger.info("Starting character download using process pool...")

    with multiprocessing.Pool() as pool:
        results = pool.map(get_character, range(1, 22))

    logger.info(
        f"Download using process pool completed in {perf_counter()-start:.2f} sec."
    )
    return [char for char in results if char is not None]


def get_characters_using_thread_pool() -> list[Character]:
    start = perf_counter()
    results: list[Character] = []

    logger.info("Starting character download using thread pool...")

    with ThreadPool(processes=20) as pool:
        results = pool.map(get_character, range(22, 42))

    logger.info(
        f"Download using thread pool completed in {perf_counter()-start:.2f} sec."
    )
    return [char for char in results if char is not None]


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


if __name__ == "__main__":
    logger.info("Starting the application.")

    total_characters: list[Character] = []

    chars = get_characters_using_process_pool()
    logger.info("Retrieved data for %d characters using process pool.", len(chars))
    total_characters.extend(chars)

    chars = get_characters_using_thread_pool()
    logger.info("Retrieved data for %d characters using thread pool.", len(chars))
    total_characters.extend(chars)

    logger.info(
        "Saving %d characters to '%s'...", len(total_characters), DATABASE_FILENAME
    )
    reset_database()
    add_characters_to_database(total_characters)
