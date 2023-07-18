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
        if(type(n)==matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    #Dot product of values in col
                    self.values[i][j] *= n.values[i][j]

        else:
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
                self.values[i][j] = random.uniform(-1, 1)



    
    def to_array(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.values[i][j])

        return arr

    def log(self):
        for i in range(self.rows):
            print(self.values[i])
        print("###################")
        return True


def map(a, fn):

    result = matrix(a.rows, a.cols)

    # appyl a function to every element of a matrix
    for i in range(a.rows):
        for j in range(a.cols):
            val = a.values[i][j]
            result.values[i][j] = fn(val)

    return result

def transpose(a):
    result = matrix(a.cols, a.rows)

    for i in range(a.rows):
        for j in range(a.cols):
            result.values[j][i] = a.values[i][j]
    
    return result

def from_array(arr):
    m = matrix(len(arr), 1)
    for i in range(len(arr)):
        m.values[i][0] = arr[i]

    return m

def subtract(a, b):
    result = matrix(a.rows, a.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            result.values[i][j] = a.values[i][j] - b.values[i][j]

    return result

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


def main():
    arr = [1, 0, -5]
    m = from_array(arr)
    print(type(m)==matrix)



if __name__ == "__main__":
    main()