def minOperations(s: str) -> int:
    res = 0
    for i, char in enumerate(s):
        # Count changes needed to make s match "0101..."
        if int(char) != i % 2:
            res += 1

    # Return the minimum of changing to "0101..." vs "1010..."
    # The sum of changes for both patterns always equals len(s)
    return min(res, len(s) - res)


print(minOperations("1100"))