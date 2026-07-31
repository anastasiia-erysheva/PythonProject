memo = {}
def tribonacci(n):
    if n <= 3:
        return 1
    if n in memo:
        return memo[n]
    result = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    memo[n] = result
    return result

print(tribonacci(45))
