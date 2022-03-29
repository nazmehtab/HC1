import sys

n = int(input('Enter total number of entries : '))
dict = {}
print('Entries are : ')
for i in range(n):
    contact = input().split()
    dict[contact[0]] = contact[1]
while True:
    try:
        name = input('Enter name : ').strip()
        if name in dict:
            print(f'{name} = {str(dict[name])}')
        else:
            print('Not found')
    except EOFError:
        break
