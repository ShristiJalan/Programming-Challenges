for _ in range (int(input())):
    rev = 0
    num = int(input())
    while(num > 0):
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    print(rev)