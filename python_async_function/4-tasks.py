#!/usr/bin/env python3
"""
Module pour la tâche 4.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n fois avec le max_delay spécifié.

    Retourne la liste des délais (floats) par ordre croissant.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    # asyncio.as_completed récupère les tâches dès qu'elles finissent
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
