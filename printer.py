class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # Start with the worst case (printing each character separately)
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]  # If characters are the same, reduce the problem size
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        
        return dp[0][n-1]

# Example usage:
s = "aaabbb"
solution = Solution()
print(solution.strangePrinter(s))  # Output: 2

s = "aba"
print(solution.strangePrinter(s))  # Output: 2
