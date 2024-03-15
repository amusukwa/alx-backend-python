#!/usr/bin/env python3
"""Module for the safe_first_element function."""
from typing import Any, Iterable, Union


def safe_first_element(lst: Iterable[Any]) -> Union[Any, None]:
    """Return the first element of an iterable or None if it's empty."""
    if lst:
        return lst[0]
    else:
        return None
