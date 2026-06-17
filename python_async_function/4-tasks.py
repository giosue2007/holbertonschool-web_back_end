#!/usr/bin/env python3
"""
Tasks module.
"""
import asyncio
from typing import List

# Import task_wait_random from the previous task file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    
    Returns the list of all the delays (float values) in ascending order
    without using sort() because of concurrency.
    """
    # Create a list of asyncio.Task objects by calling task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    delays = []
    # Use asyncio.as_completed to yield tasks as they finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
