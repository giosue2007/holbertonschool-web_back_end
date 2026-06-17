#!/usr/bin/env python3
"""
Module pour la tâche 1 : Async Comprehensions.
"""
from typing import List

# Import de async_generator depuis le fichier précédent
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Récupère 10 nombres aléatoires générés par async_generator
    en utilisant une compréhension de liste asynchrone.
    """
    return [i async for i in async_generator()]
