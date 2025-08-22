def min_deletions_palindrome(s: str) -> int:
    n = len(s)

    # Longest Palindromic Subsequence (LPS) using DP
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    
    lps = dp[0][n-1]
    return n - lps

s = "aebcbda"
print(min_deletions_palindrome(s))  # Output: 2
