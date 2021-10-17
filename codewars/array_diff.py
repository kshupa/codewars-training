def array_diff(a, b):
    """Return list resulted from subracting one list from another."""
    c = []

    for i in a:
        if i not in b:
            c.append(i)

    return c
