def binary_search(array, num):
    left_el = 0
    right_el = len(array) - 1

    def check(left, right):
        if right >= left:
            mid = (left + right) // 2

            if array[mid] == num:
                return mid
            elif array[mid] < num:
                return check(mid + 1, right)
            else:
                return check(left, mid - 1)
        else:
            return -1

    return check(left_el, right_el)


input_array = list(map(int, input("Введите элементы массива через пробел: ").split()))
input_num = int(input("Введите искомое число: "))
print(f"Результат: {binary_search(input_array, input_num)}")
