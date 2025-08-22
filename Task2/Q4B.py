def good_subarrays(a):
    n = len(a)
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s % (j - i + 1) == 0:
                count += 1
    return count

n = 4
a = [2, 4, 6, 2]
print(good_subarrays(a))  # Output: 9
