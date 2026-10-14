#!/usr/bin/env python3
"""
Module defining a regular function that returns an asyncio.Task.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: Task wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
