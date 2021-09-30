class Matrix:
    my_list = []

    def __init__(self, my_list):
        self.list = my_list

    def __str__(self):
        print(' ')
        res = ''
        for i in range(len(self.list)):
            res += str(self.list[i]) + '\n'
        return res

    def __add__(self, other):
        res = []
        a = self.list
        b = other.list
        for i in range(len(a)):
            if i >= len(b):
                b.append([])
            res.append([])
            for j in range(len(a[i])):
                if j >= len(b[i]):
                    b[i].append(0)
                res[i].append(a[i][j] + b[i][j])
        return Matrix(res)


matrix1 = Matrix([[1, 5, 9], [1, 4, 5], [4, 8, 9]])
print(matrix1)

matrix2 = Matrix([[1, 5, 7], [6, 8, 9]])
print(matrix2)

matrix3 = matrix1 + matrix2
print(matrix3)
