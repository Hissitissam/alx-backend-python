#!/usr/bin/env pyton3
"""Module for the first task"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds."""
    wait_delay = random.uniform(0, max_delay)
    await asyncio.sleep(wait_delay)
    return wait_delay
