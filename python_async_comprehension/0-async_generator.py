#!/usr/bin/env python3
"""
Module defining an asynchronous generator yielding random floats.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, waits asynchronously for 1 second at each iteration,
    and yields a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
