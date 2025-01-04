from collections import deque
import copy

def simulate_plague_spread(grid):
    """
    Simulate plague spread for one day based on given rules.
    
    Args:
        grid (list): 2D grid representing city infection status
    
    Returns:
        list: Updated grid after one day of plague spread
    """
    N = len(grid)
    new_grid = [row[:] for row in grid]
    
    # Directions for 8 neighboring cities
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    def count_infected_neighbors(row, col):
        """Count infected neighbors for a given cell."""
        infected_count = 0
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < N and 0 <= new_col < N and grid[new_row][new_col] == '1':
                infected_count += 1
        return infected_count
    
    # Apply plague spread rules
    for row in range(N):
        for col in range(N):
            if grid[row][col] in ['0', 's', 'd']:
                # Uninfected city (potential infection)
                infected_neighbors = count_infected_neighbors(row, col)
                if infected_neighbors == 3:
                    new_grid[row][col] = '1'
            elif grid[row][col] == '1':
                # Infected city
                infected_neighbors = count_infected_neighbors(row, col)
                if infected_neighbors < 2 or infected_neighbors > 3:
                    new_grid[row][col] = '0'
    
    return new_grid

def find_minimum_days(grid):
    """
    Find minimum days to reach herb city avoiding plague spread.
    
    Args:
        grid (list): Initial state grid
    
    Returns:
        int: Minimum days to reach herb city
    """
    N = len(grid)
    
    # Find source and destination coordinates
    source = destination = None
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 's':
                source = (row, col)
            elif grid[row][col] == 'd':
                destination = (row, col)
    
    # Possible movements (stay or move to adjacent cities)
    movements = [
        (0, 0),   # Stay
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    
    # BFS queue: (current_grid, current_pos, days_spent, path)
    queue = deque([(grid, source, 0, [source])])
    visited = set()
    
    while queue:
        current_grid, (current_row, current_col), days, path = queue.popleft()
        
        # Check if reached destination
        if (current_row, current_col) == destination:
            return days
        
        # Create grid state key for visited tracking
        grid_state = tuple(tuple(row) for row in current_grid)
        current_pos_state = (current_row, current_col)
        visited_key = (grid_state, current_pos_state)
        
        if visited_key in visited:
            continue
        visited.add(visited_key)
        
        # Simulate plague spread for next day
        next_day_grid = simulate_plague_spread(current_grid)
        
        # Explore possible movements
        for dx, dy in movements:
            new_row, new_col = current_row + dx, current_col + dy
            
            # Check movement validity
            if (0 <= new_row < N and 0 <= new_col < N and 
                next_day_grid[new_row][new_col] not in ['1']):
                
                # Deep copy grid to prevent modification
                new_grid = [row[:] for row in next_day_grid]
                new_grid[current_row][current_col] = '0'  # Clear current position
                new_grid[new_row][new_col] = 's'  # Mark new position
                
                # Create new path
                new_path = path + [(new_row, new_col)]
                
                queue.append((new_grid, (new_row, new_col), days + 1, new_path))
    
    return -1  # Unreachable scenario

def main():
    # Read grid size
    N = int(input())
    
    # Read grid
    grid = []
    for _ in range(N):
        grid.append(list(input().strip()))
    
    # Find minimum days
    result = find_minimum_days(grid)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()