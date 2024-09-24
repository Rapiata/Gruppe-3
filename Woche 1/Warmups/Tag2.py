def multiply_numbers(arr):

    # edge cases, array too short
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    result = 1
    for i in arr:
        if i == 0:
            return 0

        # edge case, i is not numeric
        if type(i) != int and type(i) != float:
            return "Error"
        result *= i

    return result


arr = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 0, 5]
arr3 = []
arr4 = [1]
arr5 = [1, 2, 3, "a", 5]

print(multiply_numbers(arr))
print(multiply_numbers(arr2))
print(multiply_numbers(arr3))
print(multiply_numbers(arr4))
print(multiply_numbers(arr5))
