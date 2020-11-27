lst=[]
sum = 0
n = int(input())
for i in range(n):
    lst.append(int(input()))
lst.sort()

x = n//4
lstx = []
for j in range(x):
    lstx.append(4+(4*j))

# print(lst,lstx)

res = [lst[i : j] for i, j in zip([0] + 
          lstx, lstx + [None])]

for v in range(x):
    sum = sum + res[v][1]

print(sum)

