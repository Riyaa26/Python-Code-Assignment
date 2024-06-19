def count_occurrences(lst, element):
    return lst.count(element)

numbers_list = [1, 2, 3, 4, 5, 2, 3, 2, 1]
element_to_count = 2
occurrences_count = count_occurrences(numbers_list, element_to_count)
print(occurrences_count)
