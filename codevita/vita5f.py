from itertools import combinations
import math

# Function to calculate the area of a polygon using the Shoelace formula
def polygon_area(vertices):
    vertices.append(vertices[0])  # Add the first vertex at the end
    n = len(vertices)
    area = 0
    for i in range(n-1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i+1]
        area += x1 * y2 - x2 * y1
    return abs(area) // 2

# Function to find the maximum polygon area formed by the line segments
def max_polygon_area(n, segments):
    points = set()
    for x1, y1, x2, y2 in segments:
        points.add((x1, y1))
        points.add((x2, y2))
    
    max_area = 0
    for comb in combinations(points, 3):
        area = polygon_area(list(comb))
        if area > max_area:
            max_area = area
            
    return max_area

# Example input
n = 5
segments = [
    (2, 1, 2, 6),
    (5, 1, 5, 6),
    (0, 2, 6, 2),
    (0, 5, 6, 5),
    (0, 0, 6, 6)
]

# Calculate and print the maximum enclosed area
print(max_polygon_area(n, segments)) # Output: 9
