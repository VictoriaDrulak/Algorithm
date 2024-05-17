def sorting_algorithm_1(list_of_numbers):
    new_list = []
    while len(list_of_numbers) > 0:
        for x in list_of_numbers:
            if x == min(list_of_numbers):
                list_of_numbers.remove(x)
                new_list.append(x)
    return new_list

print(sorting_algorithm_1([3, 2, 9, 7, 1, 4]))

def sorting_algorithm_2(list_of_numbers):
    lenght = len(list_of_numbers)
    for x in range(lenght):
        for y in range(0, lenght - x - 1):
            if list_of_numbers[y] > list_of_numbers[y + 1]:
                list_of_numbers[y], list_of_numbers[y + 1] = list_of_numbers[y + 1], list_of_numbers[y]
    return list_of_numbers

print(sorting_algorithm_2([3, 2, 9, 7]))