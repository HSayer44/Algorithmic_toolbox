
def binary_search_multiple(keys, queries):
    result = []
    for q in queries:
        left, right = 0, len(keys) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if keys[mid] == q:
                index = mid
                break
            elif keys[mid] < q:
                left = mid + 1
            else:
                right = mid - 1
        result.append(index)
    return result



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_multiple(input_keys, q), end=' ')
