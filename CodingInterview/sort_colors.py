from typing import List


def sort_colors(colors: List[int]) -> List[int]:
    i = j = 0
    k = len(colors)

    while j < k:
        if colors[j] < 1:
            colors[i], colors[j] = colors[j], colors[i]
            i += 1
            j += 1
        elif colors[j] > 1:
            k -= 1
            colors[j], colors[k] = colors[k], colors[j]
        else:
            j += 1
        print(colors)

    print(i, j, k)

    return colors


print(sort_colors([2, 0, 2, 1, 1, 0, 1, 2, 0, 0, 1, 2]))
