def counting_sort(arr):
    counts = [0]*(max(arr) + 1)
    for ele in arr:
        counts[ele] += 1
    # prefix counts
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    sorted_array = [0] * len(arr)
    for ele in arr[::-1]:
        index = counts[ele] - 1
        sorted_array[index] = ele
        counts[ele] -= 1
    return sorted_array
