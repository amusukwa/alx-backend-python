#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string k and an int/float v into a tuple (k, v^2)."""
    return (k, v ** 2)
