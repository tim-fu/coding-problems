def diagonal_traverse(mat: list[list[int]]) -> list[int]:
    """LC 498"""
    diagonal_order = []
    m = len(mat)
    n = len(mat[0])
    is_reversed = True

    for i in range(n):
        current_diagonal = []
        row = 0
        col = i

        while col > -1 and row < m:
            current_diagonal.append(mat[row][col])
            row += 1
            col -= 1

        if is_reversed:
            current_diagonal.reverse()
            diagonal_order.extend(current_diagonal)
        else:
            diagonal_order.extend(current_diagonal)
        is_reversed = not is_reversed

    for j in range(1, m):
        current_diagonal = []
        row = j
        col = n - 1

        while row < m and col > -1:
            current_diagonal.append(mat[row][col])
            row += 1
            col -= 1

        if is_reversed:
            current_diagonal.reverse()
            diagonal_order.extend(current_diagonal)
        else:
            diagonal_order.extend(current_diagonal)
        is_reversed = not is_reversed

    return diagonal_order
                    
