from random import randint

def partition3(array, left, right):
    pivot = array[left]
    i = left
    j = left
    k = right
    while j <= k:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
        elif array[j] == pivot:
            j += 1
        else:
            array[j], array[k] = array[k], array[j]
            k -= 1
    return i, k



def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
