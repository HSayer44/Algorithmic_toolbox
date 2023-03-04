from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # sort the segments by their end points
    segments = sorted(segments, key=lambda x: x.end)
    # initialize the current point as the first end point
    current_point = segments[0].end
    points.append(current_point)
    # iterate through the segments to find the points
    for s in segments:
        # if the current point doesn't cover the current segment,
        # add the segment's end point as the new current point
        if current_point < s.start or current_point > s.end:
            current_point = s.end
            points.append(current_point)
    return points


if __name__ == '__main__':
    input_data = stdin.read().strip()
    n, *data = map(int, input_data.split())
    segments = [Segment(data[i], data[i+1]) for i in range(0, len(data), 2)]
    points = optimal_points(segments)
    print(len(points))
    print(*points)

