def nice_pairs(a, k):
    n = len(a)
    freq = [0] * k
    for num in a:
        freq[num % k] += 1

    count = (freq[0] * (freq[0] - 1)) // 2
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += freq[i] * freq[k - i]
    if k % 2 == 0:
        count += (freq[k // 2] * (freq[k // 2] - 1)) // 2

    return count

n, k = 5, 3
a = [1, 2, 3, 4, 5]
print(nice_pairs(a, k))  # Output: 4
