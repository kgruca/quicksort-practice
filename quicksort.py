# # def quick_sort(array):
# #     if len(array) < 2:
# #         return array
# #     else:
# #         pivot = array[0]
# #         less = [i for i in array[1:] if i <= pivot]
# #         greater = [i for i in array[1:] if i > pivot]

# #         return quick_sort(less) + [pivot] + quick_sort(greater)


# # quick_sort_arr = [1, 78, 34, 98, 112, 4, 0, 57]

# # print(quick_sort(quick_sort_arr))


# def quicksrt(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         low = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]

#         return quicksrt(low) + [pivot] + quicksrt(greater)


# new_quicksrt_arr = [789, 45, 98, -5, 43, 11, 8, 14, 99, 156, 15]

# print(quicksrt(new_quicksrt_arr))
import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.randint(0, len(arr) - 1)
        low = [i for i in arr[]]
        


















