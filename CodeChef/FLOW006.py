# lst=[]
# sum = 0
# for i in range(int(input())):
#     a = int(input())
#     while(a != 0):
#         lst.append(a%10)
#         a = a//10
#     for ii in range (len(lst)):
#         sum = sum + lst[ii]
#     print(sum)
    
# for i in range(int(input())):
#     sum = 0
#     x = int(input())
#     while(x>0):
#         sum = sum + x%10
#         x = x//10
#     print(sum)
lst = []
for _ in range (int(input())):
    lst = [int(x) for x in input()] #list comprehension
    print(sum(lst))