#!/usr/bin/env python3
'''A module for task 1 that is a write a coroutine called async_comprehension 
that takes no arguments.'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates a list of 10 random numbers from a 10-number generator."""
    return [num async for num in async_generator()]
