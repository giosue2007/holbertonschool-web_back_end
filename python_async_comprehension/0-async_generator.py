#!/usr/bin/env python3
"""
Module pour la tâche 0 : Async Generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Générateur asynchrone qui boucle 10 fois.
    Attend 1 seconde à chaque itération et yield un nombre aléatoire.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
