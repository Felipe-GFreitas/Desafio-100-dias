import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

a.sort()
b.sort()
lower_b = a[n - 1];
upper_b = b[0] + 1;
l = []
for i in range(upper_b - lower_b):
    num = i + lower_b
    flag = 1;
    for j in range(n):
        if(num % a[j] != 0):
            flag = 0
            break
    for j in range(m):
        if(b[j] % num != 0):
            flag = 0
            break
    if(flag == 1):
        l.append(num)
    
print(len(l))