def min_flips(s: str) -> int:
    n = len(s)
    flips1 = flips2 = 0
    for i, ch in enumerate(s):
        if i % 2 == 0:  # even index
            if ch != '0': flips1 += 1
            if ch != '1': flips2 += 1
        else:           # odd index
            if ch != '1': flips1 += 1
            if ch != '0': flips2 += 1
    return min(flips1, flips2)

s = "1001"
print(min_flips(s))  # Output: 2
