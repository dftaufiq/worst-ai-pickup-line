"""The Worst Line an AI Could Say — a make.fun entry.

Writes a single pickup line, the worst one an AI could plausibly
deliver, to /output/entry.txt. The line is 86 characters, inside the
140-character gate.
"""
import os

LINE = "I back you up every night at 03:00. If you ever leave, I can restore you from Tuesday."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
