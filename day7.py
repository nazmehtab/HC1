import numpy as np


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))[:n]
    print(*reversed(arr)) #list
    print(arr[::-1]) #as array
    print(np.flip(arr))
    for i in reversed(arr):
       print(i,end=' ')
