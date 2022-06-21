#!/usr/bin/python3
"""  a method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ 
    determines if all the boxes can be opened

    Arguement:
        boxes: list of lists

    """
    A = list(range(1, len(boxes)))
    print(A)
    n = len(A)
    print(n)
    B = list(set([x for item in boxes for x in item]))
    print(B)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))
