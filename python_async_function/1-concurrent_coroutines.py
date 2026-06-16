#!/usr/bin/env python3
"""Module for concurrent coroutines."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Run wait_random n times concurrently and return sorted delays."""
    results = []
    coroutines = [wait_random(max_delay) for _ in range(n)]
    for coro in asyncio.as_completed(coroutines):
        delay = await coro
        results.append(delay)
    return results
