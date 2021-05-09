def reverse_list1(arr):
    return arr[::-1]

def reverse_list2(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)
    arr = new_arr
    return arr
