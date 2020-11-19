for i in range(int(input())):
    n = int(input())
    ld = n%10
    while(n > 10):
        n = n//10
    fd = n
    print(ld+fd)