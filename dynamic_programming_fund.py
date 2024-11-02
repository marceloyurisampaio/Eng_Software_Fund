#De forma geral são duas tecnicas utilizadas em programação dinamica, memoization (top-down) e tabulação (bottom-up). 
#O problema da sequência de fibonacci pode ser resolvido utilizando memoização ou não. 

#Fibo sem DP
def fibonacci(n):
  if n <= 1: 
    return n
  else: 
    return fibonacci(n-1) + fibonacci(n-2)
#O problema dessa implementação é que um mesmo resultado e calculado diversas vezes. 

#Fibo com DP
fib_cache = {}

def fibonacci_dp (n):
  if n in fib_cache:
    return fib_cache[n]
  if n <= 1: 
    fib_cache[n] = n
  else: 
    fib_cache[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)
  return fib_cache[n]


def longest_palindromic_subsequence(A):
    n = len(A)
    B = A[::-1]  # String reversa de A

    # Inicializa a matriz DP
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Preenche a matriz DP
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # O comprimento da maior subsequência palindrômica
    return dp[n][n]

# Exemplo de uso:
A = "bebeeed"
resultado = longest_palindromic_subsequence(A)
print(f"O comprimento da maior subsequência palindrômica é: {resultado}")

def longest_common_subsequence(A, B):
    m, n = len(A), len(B)
    # Initialize the DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                # Characters match, extend the LCS by 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters do not match, take the maximum of adjacent values
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of LCS is in the bottom-right cell
    return dp[m][n]

# Example usage:
A = "abbcdgf"
B = "bbadcgf"
result = longest_common_subsequence(A, B)
print(f"The length of the longest common subsequence is: {result}")



