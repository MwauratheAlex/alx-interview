#!/usr/bin/python3
"""Lock boxes module"""


def canUnlockAll(boxes):
    """Returns true if all boxes can be unlocked else false"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]
    while stack:
        curr = stack.pop()

        if not unlocked[curr]:
            continue

        for key in boxes[curr]:
            if 0 <= key < n and not unlocked[key]:
                stack.append(key)
                unlocked[key] = True

    return all(unlocked)
