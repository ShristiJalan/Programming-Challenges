for i in range(int(input())):
    lst = []
    a, b = map(int, input().split())
    if(a > b):
        lead = a-b
    else:
        lead = b-a
    lst = lst.append(lead)
    print(max(lst))