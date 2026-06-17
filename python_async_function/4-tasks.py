#!/usr/bin/env python3
"""
Module pour la tâche 4.
"""
import asyncio
from typing import List

# Import de task_wait_random depuis le fichier précédent
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n fois avec le max_delay spécifié.

    Retourne la liste des délais (floats) par ordre croissant
    grâce à asyncio.as_completed.
    """
    # Création de la liste de Tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    # asyncio.as_completed récupère les tâches au fur et à mesure de leur réussite
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
