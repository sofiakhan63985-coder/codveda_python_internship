def solve_nqueens(n):
    if n <= 0:
        return []

    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 1:
                return False

        return True

    def backtrack(row):
        if row == n:
            solutions.append([board[r][:] for r in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    return solutions


def print_board(solution):
    for row in solution:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


if __name__ == "__main__":
    n = 4
    solutions = solve_nqueens(n)
    print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print_board(sol)