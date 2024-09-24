"""
Schreiben Sie eine Python-Funktion, die alle Zahlen in einem Array addiert und die Summe zurückgibt. 
Alle Zahlen, die für die Summe verwendet wurden, müssen aus dem Array entfernt werden. 
Geben Sie die Summe und die verbleibenden Elemente des Arrays zurück, die nicht für die Summierung verwendet werden konnten.
"""


def sum_and_remove(arr):
    sum = 0
    idx = 0

    while idx < len(arr):
        if type(arr[idx]) == int or type(arr[idx]) == float:
            sum += arr[idx]
            arr.pop(idx)
        else:
            idx += 1

    return sum, arr


array = [1, 2, 34, True, None, "1", 3.5]
print(sum_and_remove(array))  # returns -> (40.5, [True, None, "1"])
