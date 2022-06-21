#!/usr/bin/python3
"""  a method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ 
    determines if all the boxes can be opened

    Arguement:
        boxes: list of lists

    """
    A = list(range(1, len(boxes)))
    n = len(A)
    B = list(set(x for item in boxes for x in item))
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))
