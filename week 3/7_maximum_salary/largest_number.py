"""
n the case of "23" and "92", the first characters "2" and "9" are compared. Since "9" comes after "2" in the ASCII character set (which is used to represent characters as numbers), "92" is considered larger than "23". If the first characters were the same, the second characters would be compared, and so on.
By multiplying each string by 3, we effectively compare all the digits of the strings, from left to right. This way, we can ensure that the resulting concatenated number is as large as possible."""

from itertools import permutations

def largest_number(numbers):
    # Convert the list of integers to a list of strings
    numbers = list(map(str, numbers))

    # Sort the list of strings in descending order using a custom sorting key
    numbers.sort(key=lambda x: x*3, reverse=True)

    # Concatenate the sorted strings into a single string and convert it to an integer
    largest = int("".join(numbers))

    # Return the largest integer
    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
