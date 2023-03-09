from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared(points):
    if len(points) <= 1:
        return float('inf')

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    left_min_distance_squared = minimum_distance_squared(left_points)
    right_min_distance_squared = minimum_distance_squared(right_points)

    min_distance_squared = min(left_min_distance_squared, right_min_distance_squared)

    strip_points = []
    for point in points:
        if abs(point.x - points[mid].x) < sqrt(min_distance_squared):
            strip_points.append(point)

    strip_points.sort(key=lambda point: point.y)

    for i in range(len(strip_points)):
        for j in range(i + 1, len(strip_points)):
            if (strip_points[j].y - strip_points[i].y) ** 2 >= min_distance_squared:
                break
            min_distance_squared = min(min_distance_squared, distance_squared(strip_points[i], strip_points[j]))

    return min_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    input_points.sort(key=lambda point: point.x)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))

