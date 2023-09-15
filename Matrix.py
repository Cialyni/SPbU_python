class Matrix:

    def __init__(self, n=0, m=0, lst=[]):
        self.matrix = lst
        self.n = n
        self.m = m

    def __add__(self, other):
        ans = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                ans[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(self.n, self.m, ans)

    def __sub__(self, other):
        ans = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                ans[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(self.n, self.m, ans)

    def __mul__(self, other):
        ans = [[0 for j in range(other.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                ans[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.m))
        return Matrix(self.n, other.m, ans)

    def transponirovanie(self):
        ans = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                ans[j][i] = self.matrix[i][j]
        self.matrix = ans

    def input(self, number_of_matrix=1):
        print('\nEntering matrix №{}: '.format(number_of_matrix))
        print('Input matrix size N, M: ')
        n, m = map(int, input().split())
        print('Input matrix: ')
        return Matrix(n, m, [list(map(int, input().split())) for i in range(n)])

    def output(self):
        for elem in self.matrix:
            print(*elem)
