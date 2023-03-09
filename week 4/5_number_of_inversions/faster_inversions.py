def merge_and_count(left, right):
    result = []
    i = j = count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result += left[i:]
    result += right[j:]
    return result, count

def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, lcount = count_inversions(a[:mid])
    right, rcount = count_inversions(a[mid:])
    merged, mcount = merge_and_count(left, right)
    return merged, lcount + rcount + mcount

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    _, count = count_inversions(elements)
    print(count)

