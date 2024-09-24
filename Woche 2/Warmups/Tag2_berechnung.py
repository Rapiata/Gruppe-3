def sum_from_range(n):
    summe = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            summe += i
    return summe
