#!/usr/bin/env python3
"""
Module pour la tâche 2 : Temps d'exécution de 4 compréhensions.
"""
import asyncio
import time

# Import de async_comprehension depuis le fichier précédent
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension 4 fois en parallèle avec asyncio.gather
    et mesure le temps d'exécution total.
    """
    start_time = time.perf_counter()

    # Exécution des 4 tâches en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
