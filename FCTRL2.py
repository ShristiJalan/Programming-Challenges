
for i in range(int(input())):
    a = int(input())
    if a==0:
        print("1")
    else:
        b = 1
        for c in range(1, a+1):
            b = b*c
    print(b)