def factorial(k):
    if k<=1:
        return 1
    else:
        return k * factorial(k-1)

def euler(n):
    if n==0:
        return 1
    else:
        return (1/factorial(n)) + euler(n-1)
print(f'euler(20) = {euler(20):.5f}')