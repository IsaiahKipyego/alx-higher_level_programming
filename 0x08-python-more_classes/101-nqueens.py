#!/usr/bin/python3
"""
Solves n-queens problem
This is an N*N chess board where N queens are placed in a way
that they cannot capture each other
"""


def check_safe(board, row, col):
    """
    Checks if position is safe

    Args:
        board: current state of board
        row: row that is being checked
        col: column that is being checked
    Return:
        returns either True or False
    """
    # checks if queen can be captured
    for i in range(col):
        if board[i] is row or abs(board[i] - row) is abs(i - col):
            return False
    return True


def check_board(board, col):
    """
    Checks board state of column using backtracking

    Args:
        board: state of the board
        col: column being checked
    """
    n = len(board)
    if col is n:  # if all items have been iterated
        print(str([[c, board[c]] for c in range(n)]))
        return

    for row in range(n):  # iterate checking if position is safe
        if check_safe(board, row, col):
            board[col] = row
            check_board(board, col + 1)


if __name__ == "__main__":
    """
    driver of the program
    """
    import sys

    if len(sys.argv) != 2:
        print("usage: nqueens N")
        sys.exit(1)

    n = 0
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0 for col in range(n)]
    check_board(board, 0)
