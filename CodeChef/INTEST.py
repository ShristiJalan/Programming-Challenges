n, k = map(int, input().split())
count = 0;
for i in range(n):
   ti =  int(input())
   if(ti % k == 0): 
       count = count + 1
print(count)
