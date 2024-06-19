def min_max_values(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

numbers_list = [10, 5, 8, 3, 15, 7]
min_value, max_value = min_max_values(numbers_list)
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
