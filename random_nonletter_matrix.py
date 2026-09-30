"""Print a 10×10 matrix made of random non-letter characters."""

from __future__ import annotations

import random
import string


SIZE = 10
# Digits and punctuation are all non-letter printable ASCII characters.
SYMBOLS = string.digits + string.punctuation


def generate_matrix(size: int = SIZE) -> list[list[str]]:
    """Return a square matrix of random characters from ``SYMBOLS``."""
    return [[random.choice(SYMBOLS) for _ in range(size)] for _ in range(size)]


def print_matrix(matrix: list[list[str]]) -> None:
    """Write a matrix to standard output, one space-separated row per line."""
    for row in matrix:
        print(" ".join(row))


def main() -> None:
    print_matrix(generate_matrix())


if __name__ == "__main__":
    main()
