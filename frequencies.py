"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items = list(map(str, items));
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1;
        else:
            frequencies[item] = 1;
    # Your code goes here
    return frequencies

