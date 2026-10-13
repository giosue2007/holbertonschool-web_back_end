#!/usr/bin/env python3
"""
Module executing multiple coroutines concurrently.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay and returns the list of delays
    in ascending order of completion (without using sort()).

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delay values sorted in ascending order of arrival.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
