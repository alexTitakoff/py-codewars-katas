# https://www.codewars.com/kata/find-the-odd-int/train/python
# найти последнее нечетное число

# Учитывая массив, найдите int, который появляется нечетное количество раз.
# Всегда будет только одно целое число, которое появляется нечетное количество раз.

# 1.Найти несчетные
# 2. Посчитать их количества раз
# 3. Если колчество тоже нечетное вынести число в результат

test_list = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,7,7,-1]

seq = test_list


def list_odd_num_func(list):
    odd_list_nums = []

    for el in list:
        if el % 2 != 0:
            odd_list_nums.append(el)

    return odd_list_nums


def count_num_in_list(num, list):
    count = 0
    for el in list:
        if el == num:
            count += 1

    return count




def find_it(seq):

    res = 10

    list_odd_num = list_odd_num_func(seq)

    for el in list_odd_num:
        if count_num_in_list(el,seq) % 2 != 0:
            res = el
    print(res)
    return res


find_it(seq)





