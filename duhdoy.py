"""Sarcasm."""

from itertools import cycle

case = cycle(["lower", "upper"])


def print(text):
    """Textual Sarcasm."""
    generated = ""
    for char in text:
        generated += getattr(char, next(case))()
    return generated
