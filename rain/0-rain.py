#!/usr/bin/python3
"""
    Calculate the amount of rainwater retained between walls.

    Given a list of non-negative integers representing the heights of walls
    with unit width 1, as if viewing the cross-section of a relief map, this
    function calculates how many square units of water will be retained after
    it rains.
"""


def calculate_water_consumptions(list, n):
    max_size = 0

    if not wall:
        return 0

    for i in range(1, n-1):
        left_max = list[i]
        for j in range(i):
            left_max = max(left_max, list[j])
            right_max = list[i]
        for j in range(i + 1, n):
            right_max = max(right_max, list[j])
        max_size = max_size + (min(left_max, right_max) - list[j])
    return max_size


def rain(walls):
    water_remained = calculate_water_consumptions(walls, len(walls))
    return water_remained
