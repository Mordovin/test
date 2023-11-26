example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    i = 0
    last_index = len(data)-1
    swapped = True
    while swapped:
        swapped = False
        for i in range(last_index):
            if i < last_index:
                if data[i] > data[i + 1]:
                    data[i], data[i+1] = data[i + 1], data[i]
                    swapped = True
        if swapped:
            last_index -= 1
    return data


print(bubble_sort(example_array))


data = [-1, -4, 8, -7, 3, 0, 1, -7, -7, 0, 0, -4, 1]
# Накопительная сумма
cumulative_sums = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4]

print(len(data), len(cumulative_sums))