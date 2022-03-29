n = int(input('Enter the Decimal num : ').strip())
bi = []
while n > 0:
    b = n % 2
    bi.append(b)
    n = n // 10
print(bi)
maxi = 0
count = 0
for i in bi:
    if i == 1:
        count += 1
        if maxi < count:
            maxi = count
    else:
        count = 0
print(maxi)

# one liner solution
# print(len(max(bin(int(input().strip()))[2:].split('0'))))


def func(num):
    return num[2:]


n1 = int(input().strip())
a = max(func(bin(n1)).split('0')).count('1')
print(a)
