from sys import stdin

def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)
    
    # Combine points and their index into a list of tuples
    combined_points = [(point, index) for index, point in enumerate(points)]
    
    # Sort segments and combined points by their start and point values, respectively
    sorted_segments = sorted(zip(starts, ends))
    sorted_points = sorted(combined_points)
    
    # Initialize variables
    current_segment_index = 0
    segments = []
    
    # Iterate through sorted points and add segments as they are reached
    for point, point_index in sorted_points:
        # Add all segments that start at or before the current point
        while current_segment_index < len(sorted_segments) and sorted_segments[current_segment_index][0] <= point:
            segments.append(sorted_segments[current_segment_index][1])
            current_segment_index += 1
        # Remove segments that end before the current point
        while len(segments) > 0 and segments[0] < point:
            segments.pop(0)
        # Update count for the current point
        count[point_index] = len(segments)
    
    return count

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)

