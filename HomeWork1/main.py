def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        min_el = numbers[i]
        max_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > min_el:
                min_el = numbers[j]
                max_index = j
        temp = numbers[i]
        numbers[i] = min_el
        numbers[max_index] = temp


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


print('Императивный стиль:')
numbers_for_imperative = [5, -9, 8, 0, -3, 7, 2]
print(f'Заданный массив:\n{numbers_for_imperative}')
sort_list_imperative(numbers_for_imperative)
print(f'Отсортированный по убыванию массив:\n{numbers_for_imperative}')

print('\nДекларативный стиль:')
numbers_for_declarative = [5, -9, 8, 0, -3, 7, 2]
print(f'Заданный массив:\n{numbers_for_declarative}')
sort_list_declarative(numbers_for_declarative)
print(f'Отсортированный по убыванию массив:\n{numbers_for_declarative}')
