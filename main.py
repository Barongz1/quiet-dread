"""Two Days of Quiet Dread — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a code review comment of at most 140 characters that approves a pull request with quiet existential dread.
"""
import os

LINE = "Approved. The code works, the tests pass, and I have no idea why — merging before it notices."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
