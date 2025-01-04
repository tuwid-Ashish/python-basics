def remove_blocks(matrix, target_code):
    n, m = len(matrix), len(matrix[0])
    visited = set()
    blocks_to_remove = set()
    
    # Function to find all cells occupied by a block
    def dfs(x, y, code):
        stack = [(x, y)]
        visited.add((x, y))
        block_cells = set()
        while stack:
            cx, cy = stack.pop()
            block_cells.add((cx, cy))
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, ny-1), (cx, ny+1)]:
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and matrix[nx][ny] == code:
                    stack.append((nx, ny))
                    visited.add((nx, ny))
        return block_cells

    # Find blocks and their positions
    for i in range(n):
        for j in range(m):
            if matrix[i][j] not in visited:
                block_cells = dfs(i, j, matrix[i][j])
                if matrix[i][j] == target_code:
                    target_block = block_cells
                else:
                    blocks_to_remove.add(frozenset(block_cells))

    # Check gravity effect and count the blocks to remove
    def will_fall(block_cells):
        for x, y in block_cells:
            if x+1 < n and matrix[x+1][y] not in (0, target_code):
                return False
        return True
    
    # Count the number of blocks to remove
    remove_count = 0
    while True:
        removable_blocks = [block for block in blocks_to_remove if will_fall(block)]
        if not removable_blocks:
            break
        for block in removable_blocks:
            for x, y in block:
                matrix[x][y] = 0
            blocks_to_remove.remove(block)
        remove_count += len(removable_blocks)
        
    return remove_count

# Example input
n, m = 5, 5
matrix = [
    [15, 12, 23, 13, 13],
    [15, 12, 14,  8, 10],
    [ 5, 11, 11,  8,  9],
    [ 5,  6,  6,  7,  7],
    [ 1,  1,  2,  3,  4]
]
target_code = 1

print(remove_blocks(matrix, target_code)) # Output: 8
