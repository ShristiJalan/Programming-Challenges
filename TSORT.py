lst = []
for i in range(int(input())):
    a = int(input())
    lst.append(a)
lst.sort(reverse=True)
print(*lst, sep = "\n")
    
    