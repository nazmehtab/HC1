import re

N = int(input().strip())
arr = []
for i in range(N):
    first_multiple_input = input().rstrip().split()
    firstName = first_multiple_input[0]
    emailID = first_multiple_input[1]
    if emailID.endswith('gmail.com'):
    #if 'gmail.com' in emailID:
    #if re.search('@gmail.com$', emailID):
        arr.append(firstName)
arr.sort()
for i in arr:
    print(i)
#print(*sorted(arr), sep='\n')