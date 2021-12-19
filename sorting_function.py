"""Вариант сортировки по разрядам наиболее быстрый, так как максимальная сложность (O(n * макс разряд)) возрастает
с увеличением максимального разряда элементов. При увеличении размера списка сложность возрастает линейно (время работы
увеличивается только за счет увеличения внутреннего цикла"""


def radix_sort(nums):
    length = len(str(max(nums)))
    n = 10
    
    for i in range(length):
        sorting = [[] for a in range(n)]
        for number in nums:
            tmp_num = (number // 10**i) % 10
            sorting[tmp_num].append(number)
            
        nums = []
        for item in sorting:
            nums += item
            
    return nums


array = [39, 47, 54, 59, 34, 41, 32]
print(array)
print(radix_sort(array))
