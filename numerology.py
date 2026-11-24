"""Pythagorean name numerology utilities.

This module implements a traditional letter-to-number mapping. It is intended
for an educational programming demonstration, not scientific prediction.
"""
import unicodedata

LETTER_VALUES = {
    **{c: 1 for c in "AJS"},
    **{c: 2 for c in "BKT"},
    **{c: 3 for c in "CLU"},
    **{c: 4 for c in "DMV"},
    **{c: 5 for c in "ENW"},
    **{c: 6 for c in "FOX"},
    **{c: 7 for c in "GPY"},
    **{c: 8 for c in "HQZ"},
    **{c: 9 for c in "IR"},
}
MASTER_NUMBERS = {11, 22, 33}


def normalize_name(name: str) -> str:
    """Remove accents and retain alphabetic characters only."""
    if not isinstance(name, str):
        raise ValueError("Name must be text.")
    decomposed = unicodedata.normalize("NFKD", name)
    ascii_text = decomposed.encode("ascii", "ignore").decode("ascii")
    letters = "".join(ch for ch in ascii_text.upper() if ch.isalpha())
    if not letters:
        raise ValueError("Enter a name containing at least one English letter.")
    return letters


def reduce_number(number: int, preserve_master: bool = True) -> int:
    """Reduce a positive integer by repeated digit-summing."""
    if number < 0:
        raise ValueError("Number cannot be negative.")
    while number > 9:
        if preserve_master and number in MASTER_NUMBERS:
            break
        number = sum(int(digit) for digit in str(number))
    return number


def calculate_name_number(name: str) -> dict:
    """Return normalized name, letter values, total and final number."""
    normalized = normalize_name(name)
    values = [{"letter": letter, "value": LETTER_VALUES[letter]} for letter in normalized]
    total = sum(item["value"] for item in values)
    final_number = reduce_number(total)
    return {
        "normalized_name": normalized,
        "letter_values": values,
        "total": total,
        "numerology_number": final_number,
    }
