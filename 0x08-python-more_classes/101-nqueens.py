#!/usr/bin/python3
"""
Solves the n-queens problem using backtracking.
Prints all solutions for placing n queens on an nxn chessboard
so that no two queens attack each other.
"""


from sys import argv

if __name__ == "__main__":
    a = []   # solution list, initialized empty
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])   # size of board
    if n < 4:
        print("N must be at least 4")
        exit(1)

    def already_exists(y):
        """Checks if a queen exists in the given y column."""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """Determines if a queen at (x, y) should be rejected.
        Checks if a queen exists in y or can attack along diagonals."""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """Clears the solution list from index x onwards."""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """Recursive backtracking function to find solutions.
        Tries different y values for a given x. If a solution is found for
        x = n-1, prints the solution. Otherwise continues recursively
        for x+1."""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)

    # Start recursive backtracking at x = 0
    nqueens(0)
