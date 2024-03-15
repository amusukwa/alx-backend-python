#!/usr/bin/env python3
"""Module get a value from a dictionary with a default value."""

from typing import Mapping, Any, TypeVar, Union

# Define a generic type variable
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Safely get a value from a dictionary with a default value."""
    if key in dct:
        return dct[key]
    else:
        return default

