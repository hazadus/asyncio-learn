"""
Подсчет частот слов, начинающихся буквой a
https://mattfowler.io/data/googlebooks-eng-all-1gram-20120701-a.gz

Sample output:
Execution time: 31.7786
len(freqs.keys())=1440378
"""
import time

freqs = {}

with open(
    "/Users/hazadus/Downloads/googlebooks-eng-all-1gram-20120701-a", encoding="utf-8"
) as file:
    lines = file.readlines()

    start = time.time()

    for line in lines:
        data = line.split("\t")
        word = data[0]
        count = int(data[2])

        if word in freqs:
            freqs[word] = freqs[word] + count
        else:
            freqs[word] = count

    end = time.time()
    print(f"Execution time: {end-start:.4f}")
    print(f"{len(freqs.keys())=}")
