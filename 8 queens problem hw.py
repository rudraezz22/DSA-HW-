def print_board(board):
    for row in board:
        print(" ".join(row))

def eightqueen(n):
    board=[["." for i in range(n)]for j in range(n)]
    col=set()
    dig1=set()
    dig2=set()
    solutions=[]

    def backtracking(r):
        if r==n:
            solutions.append([row[:] for row in board])
            return

        for c in range(n):
            if c in col or (r-c) in dig1 or (r+c) in dig2:
                continue

            board[r][c]="Q"
            col.add(c)
            dig1.add(r-c)
            dig2.add(r+c)

            backtracking(r+1)

            board[r][c]="."
            col.remove(c)
            dig1.remove(r-c)
            dig2.remove(r+c)

    backtracking(0)
    return solutions

n=8
b=eightqueen(n)
print(len(b))
print_board(b[0])
print("\n")
print_board(b[1])