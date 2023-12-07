class Matrix:
    def __init__(self, n, m, value):
        self.n = n
        self.m = m
        self.value = value

    def __str__(self):
        return f'Hang: {self.n}, cot: {self.m}'

    def add(self, s):
        add_matrix = []

        if self.n == s.n and self.m == s.m:
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    k = self.value[i][j] + s.value[i][j]

                    row.append(k)
                add_matrix.append(row)
        return add_matrix

    def sub(self, s):
        sub_matrix = []

        if self.n == s.n and self.m == s.m:
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    k = self.value[i][j] - s.value[i][j]

                    row.append(k)
                sub_matrix.append(row)
        return sub_matrix

    def mul(self,s):
        mul_matrix = []

        if self.m == s.n:
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    t = 0  # tổng các tích của hàng A vs cột B
                    for k in range(self.n):
                        t += self.value[i][k]* s.value[k][j]
                    row.append(t)
                mul_matrix.append(row)
        return mul_matrix


m1 = Matrix(2, 2, [[1, 2], [3, 4]])
m2 = Matrix(2, 2, [[2, 4], [1, 3]])
print(m1.add(m2))
print(m1.mul(m2))



