# static method

class Math:
    def __init__(self, num):
        self.num = num

    def addtoNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    
# a = Math()
# result = a.add(1, 2)
# result = Math.add(1, 2)
# print(result)

a = Math(5)
print(a.num)
a.addtoNum(6)
print(a.num)

# print(Math.add(4, 5))
print(a.add(4, 5))