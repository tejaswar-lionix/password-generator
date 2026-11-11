#!/usr/bin/env python3
"""Generate strong random passwords with the secrets module."""
import secrets
import string

SYMBOLS = "!@#$%^&*()-_=+"


def generate(length=16, upper=True, lower=True, digits=True, symbols=True):
    if length < 4:
        raise ValueError("length must be at least 4")
    pools = []
    if lower:
        pools.append(string.ascii_lowercase)
    if upper:
        pools.append(string.ascii_uppercase)
    if digits:
        pools.append(string.digits)
    if symbols:
        pools.append(SYMBOLS)
    if not pools:
        raise ValueError("enable at least one character set")
    alphabet = "".join(pools)
    chars = [secrets.choice(pool) for pool in pools]
    chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def strength(password):
    classes = sum(
        (
            any(char in string.ascii_lowercase for char in password),
            any(char in string.ascii_uppercase for char in password),
            any(char in string.digits for char in password),
            any(char in SYMBOLS for char in password),
        )
    )
    return len(password) * classes


def main():
    print(generate())


if __name__ == "__main__":
    main()


WORDS = (
    "amber", "brisk", "cobalt", "daring", "ember", "frost", "glide", "harbor",
    "ivory", "jolly", "kite", "lunar", "mellow", "north", "orbit", "pepper",
    "quartz", "river", "solar", "tidal", "umber", "vivid", "willow", "xenon",
    "yonder", "zephyr", "anchor", "bloom", "crisp", "drift", "eagle", "flame",
)


def generate_passphrase(words=4, separator="-", capitalize=True):
    if words < 3:
        raise ValueError("passphrases need at least 3 words")
    chosen = [secrets.choice(WORDS) for _ in range(words)]
    if capitalize:
        chosen = [word.capitalize() for word in chosen]
    return separator.join(chosen)
