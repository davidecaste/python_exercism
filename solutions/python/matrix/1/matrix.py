class Matrix:
    def __init__(self, matrix_string):
        lines = matrix_string.splitlines()
        rows = []
        for line in lines:
            rows.append(list(map(int, line.split())))
        self.matrix = rows

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))][index-1] 