#!/usr/bin/python3
"""
    Calculate the amount of rainwater retained between walls.

    Given a list of non-negative integers representing the heights of walls
    with unit width 1, as if viewing the cross-section of a relief map, this
    function calculates how many square units of water will be retained after
    it rains.
"""


def rain(walls):
    water_remained = 0
    
    if not walls:
        return 0

    n = len(walls)
    
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(n):
        water_remained += max(0, min(left_max[i], right_max[i]) - walls[i])

    return water_remained
