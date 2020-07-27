# problem: return two unique indices for an array, which sum to a target value
#
#
# O(n^2) method
# def twosum(array, target):
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             if target == array[i] + array[j]:
#                 return i, j

# creating non-nesting loops gives O(n), but also BAD because of the first case would repeat
def twosum(array, target):
    array_map = {}

    for i in reversed(range(len(array))):
        comp = target - array[i]
        if comp in array_map:
            return i, array_map[comp]
        else:
            array_map[array[i]] = i

print(twosum([11, 2, 1, 3, 5], 14))
