#!/usr/bin/python3
"""Lock boxes module"""


def canUnlockAll(boxes):
    """Returns true if all boxes can be unlocked else false"""
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    seen = [False] * len(boxes)

    traverse(boxes, 0, unlocked, seen)
    return all(unlocked)


def traverse(boxes, curr, unlocked, seen):
    """traverses a list of boxes recursively"""
    if seen[curr]:
        return

    seen[curr] = True
    box = boxes[curr]
    if unlocked[curr]:
        for key in box:
            if 0 <= key < len(boxes):
                unlocked[key] = True
                traverse(boxes, key, unlocked, seen)
