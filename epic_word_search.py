'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Depth-first search
def word_search(word: str, grid: list[list]):
    """Find all instances of word in NxN grid"""
    
    n = len(grid)
    result_sets = []
    
    # All 8 directions
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right (diagonal)
        (1, -1),  # down-left (diagonal)
        (-1, 1),  # up-right (diagonal)
        (-1, -1)  # up-left (diagonal)
    ]
    
    def is_valid_position(row: int, col: int) -> bool:
        """Check if position on grid"""
        return 0 <= row < n and 0 <= col < n
    
    def search_from_position(start_row: int, start_col: int, direction: tuple[int]) -> list[str]:
        """Search from given position in given direction"""
        dr, dc = direction
        coords = []
        
        # Check if word fits on grid in this direction
        end_row = start_row + (len(word) - 1) * dr
        end_col = start_col + (len(word) - 1) * dc
        if not is_valid_position(end_row, end_col):
            return None
        
        # Move through each letter
        for i in range(len(word)):
            current_row = start_row + dr * i
            current_col = start_col + dc * i
            if grid[current_row][current_col] != word[i]:
                return None
            coords.append(f"({current_row},{current_col})")
        
        return coords
    
    # Search at every grid position
    for row in range(n):
        for col in range(n):
            for direction in directions:
                result = search_from_position(row, col, direction)
                if result:
                    result_set = "-".join(result)
                    result_sets.append(result_set)
    
    print(result_sets)
    return
                    
if __name__ == "__main__":
    # Example: 5x5 grid
    grid1 = [
        ['C', 'A', 'T', 'S', 'M'],
        ['A', 'T', 'O', 'M', 'E'],
        ['T', 'O', 'M', 'S', 'T'],
        ['S', 'M', 'S', 'A', 'R'],
        ['M', 'E', 'T', 'R', 'O']
    ]
    
    # Test different words
    test_words = ["CAT", "TOM", "ATOM", "METRO"]
    
    for word in test_words:
        print(f"\n{'='*40}")
        print(f"Searching for: {word}")
        print('='*40)
        results = word_search(word, grid1)
    
    print(f"\n{'='*40}")
    print("Grid:")
    print('='*40)
    for i, row in enumerate(grid1):
        print(f"Row {i}: {' '.join(row)}")
    print(f"Coordinates are in format: (Row, Col) starting from (0,0)")
                    