# Recursive fibonacci
def fibonacci(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else: return fibonacci(n-1, k) + k*fibonacci(n-2, k)


if __name__ == '__main__':
    n = 35                  # Input num months
    k = 5                   # Input litter size
    print(fibonacci(n,k))

