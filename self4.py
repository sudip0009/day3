from pathlib import Path



path = input("enter file path: ")

LEVELS = ["INFO", "WARNING", "ERROR"] 

def read_log_file(path):
    return Path(path).read_text(encoding="utf-8")

def count_levels(text):
    counter = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }
    for line in text.splitlines():
        tokens = line.split()
        for level in LEVELS:
            if level in tokens:
                counter[level] += 1
    return counter




text = read_log_file(path)

result = count_levels(text)

print(result)


