class TriangleChecker:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if ((type(self.a) == int) | (type(self.a) == float)) == False | (int(self.a) <= 0):
            return 1
        if ((type(self.b) == int) | (type(self.a) == float)) == False | (int(self.b) <= 0):
            return 1
        if ((type(self.c) == int) | (type(self.c) == float))  == False | (int(self.c) <= 0):
            return 1
        if (self.a + self.b > self.c) & (self.a + self.c > self.b) & (self.c + self.b > self.a):
            return 3
        else:
            return 2

a, b, c = map(int, input().split()) # эту строчку не менять
tr = TriangleChecker(a,b,c)
print(tr.is_triangle())