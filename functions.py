def hello(name = 'andres'):
    print('hello ' + name)

hello('daniel')
hello()

def getsum(n1, n2):
    total = n1 + n2
    return total

print(getsum(1, 6))

getSum = lambda num1, num2 : num1 + num2

print(getSum(8, 9))