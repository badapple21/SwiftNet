import random

class matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = []

        for i in range(rows):
            self.values.append([])
            for j in range(cols):
                self.values[i].append(0)
    
    def multiply(self, n):
        # Scalar Product
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] *= n

    def map(self, fn):
        # appyl a function to every element of a matrix
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.values[i][j]
                self.values[i][j] = fn(val)

    def add(self, n):
        if type(n)==matrix:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] += n.values[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] += n

    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] = random.randint(-10, 10)

    def transpose(self):
        result = matrix(self.cols, self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                result.values[j][i] = self.values[i][j]

        return result
    
    def log(self):
        for i in range(self.rows):
            print(self.values[i])
        print("###################")
        return True


def multiply(a, b):
    #Matrix Product
    if a.cols != b.rows:
        print("Matrix Multiply Size miss match(cols must = rows)")
        return False
    
    result = matrix(a.rows, b.cols)

    for i in range(result.rows):
        for j in range(result.cols):
            #Dot product of values in col
            sum = 0
            for k in range(a.cols):
                sum += a.values[i][k] * b.values[k][j]
            
            result.values[i][j] = sum

    return result

def double(x):
    return x * 2

def main():
    a = matrix(2, 2)
    a.randomize()
    a.log()
    a.map(double)
    a.log()


if __name__ == "__main__":
    main()