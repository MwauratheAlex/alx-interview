#!/usr/bin/python3
"""Lock boxes module"""


def canUnlockAll(boxes):
    """Returns true if all boxes can be unlocked else false"""
    stack = [0]
    n = len(boxes)
    unlocked = set([0])

    while stack:
        curr = stack.pop()
        for key in boxes[curr]:
            if key not in unlocked and 0 <= key <= n:
                unlocked.add(key)
                stack.append(key)
                if len(unlocked) == n:
                    return True
    return False
