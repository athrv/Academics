
class NQnode:
    def __init__(self, N, x, y):
        self.N = N
        self.x = x
        self.y = y
        self.ld = [0] * (2*N -1)
        self.rd = [0] * (2*N -1)
        self.cl = [0] * N
        self.solutions = []
        
    def printSolution(self):
        for indx, solution in enumerate(self.solutions, 1):
            print(f"solution at index {indx} is ")
            for i in range (self.N):
                for j in range (self.N):
                    if solution[i][j] == 1:
                        print("Q", end = " ")
                    else:
                        print("_", end = " ")
                print()
            print()
        print(f"Number of solution found are {len(self.solutions)}")
        
    def NqueensUtil(self, board, col):
        if col >= self.N:
            self.solutions.append([row[:] for row in board])
            return False
        if col == self.y:
            self.NqueensUtil(board, col+1)
        for i in range (self.N):
            if i == self.x:
                continue
            if(self.ld[i-col+self.N-1] != 1 and self.rd[i+col] != 1 and self.cl[i] != 1):
                board[i][col] = 1
                self.ld[i-col+self.N-1] = self.rd[i+col] = self.cl[i] = 1
                self.NqueensUtil(board, col+1)
                board[i][col] = 0
                self.ld[i-col+self.N-1] = self.rd[i+col] = self.cl[i] = 0
        return False
        
    def solveNqueens(self):
        board = [[0 for _ in range (self.N)] for _ in range (self.N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + self.N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1
        self.NqueensUtil(board,0)
        if not self.solutions:
            print("No solution exists!!")
        else:
            self.printSolution()
            

N = int(input("enter size of board: "))
x = int(input("enter x axis location: "))
y = int(input("enter y axis location: "))

NQ = NQnode(N, x, y)
NQ.solveNqueens()