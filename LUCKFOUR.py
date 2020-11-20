lst = []

for _ in range (int(input())):
    lst = [int(x) for x in input()]
    count = 0
    for i in range(0, len(lst)):
        if lst[i]==4:
            count = count+1
    print(count)
    
    
