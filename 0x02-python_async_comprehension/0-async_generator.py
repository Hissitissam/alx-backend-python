#!/usr/bin/env python3
'''A module for task 0 is a coroutine called async_generator
that takes no arguments'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a sequence of 10 numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
