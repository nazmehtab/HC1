class Calculator:
    # since the method does not reference any class or instance attributes, you could make it a static
    @staticmethod #static method can be called without creating calculator instance
    def power(n, p):
        if n|p < 0:
            raise ValueError('n and p should be non-negative')
        else:
            return n**p


n,p = map(int, input().split())

try:
    ans = Calculator.power(n, p)
    print(ans)
except Exception as e:
    print(e)
