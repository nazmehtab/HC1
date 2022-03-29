if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    numSwaps = 0

    # Write your code here
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j+1] = temp
                numSwaps += 1
        if numSwaps == 0:
            break
    firstElement = a[0]
    lastElement = a[n - 1]
    print(a)
    print(f'Array is sorted in {numSwaps} swaps.')
    print(f'First Element: {firstElement}')
    print(f'Last Element: {lastElement}')