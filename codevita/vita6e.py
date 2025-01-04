def min_presses_to_cover_wall(vertices, M):
    # Step 1: Calculate the bounding box of the polygon
    min_x = min(vertex[0] for vertex in vertices)
    max_x = max(vertex[0] for vertex in vertices)
    min_y = min(vertex[1] for vertex in vertices)
    max_y = max(vertex[1] for vertex in vertices)

    # Step 2: Calculate the dimensions of the bounding box
    width = max_x - min_x
    height = max_y - min_y
    
    # Step 3: Calculate the number of MxM presses needed to cover the bounding box
    # Use ceiling division to calculate the number of MxM blocks along each dimension
    num_presses_x = (width + M) // M
    num_presses_y = (height + M) // M

    # Total number of presses is the product of the number of blocks in x and y directions
    return num_presses_x * num_presses_y

def main():
    # Input parsing
    N = int(input())  # Number of vertices
    vertices = []
    for _ in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    
    M = int(input())  # Size of the brush (MxM)

    # Calculate the minimum number of presses to cover the wall
    result = min_presses_to_cover_wall(vertices, M)
    
    # Output the result
    print(result)

if __name__ == "__main__":
    main()


