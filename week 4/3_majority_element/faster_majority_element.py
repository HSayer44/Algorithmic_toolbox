# The algorithm is called "Boyer-Moore Majority Vote Algorith"

def majority_element(elements):
    candidate = elements[0]
    count = 1
    for i in range(1, len(elements)):
        if elements[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = elements[i]
                count = 1

    count_candidate = 0
    for e in elements:
        if e == candidate:
            count_candidate += 1

    if count_candidate > len(elements) / 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

