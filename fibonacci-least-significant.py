def solution(n):
    fibs = {0: 0, 1: 1}
    def fibonacci(n):
        if n in fibs: 
            return fibs[n]
        if n % 2 == 0:
            fibs[n] = ((2 * fibonacci((n / 2) - 1)) + fibonacci(n / 2)) * fibonacci(n / 2) % 1000000
            return fibs[n]
        else:
            fibs[n] = (fibonacci((n - 1) / 2) ** 2) + (fibonacci((n+1) / 2) ** 2) % 1000000
            return fibs[n]
    sixleastSD = fibonacci(n)
    return sixleastSD % 1000000

print(solution(36))
