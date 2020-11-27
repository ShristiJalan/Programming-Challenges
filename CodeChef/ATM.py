x, y = input().split()
x = int(x)
y = float(y)
# if (x % 5 == 0 and x < y):
#     print('%.2f' % (y-x-0.5))
# else:
#     print('%.2f' % y)
if (x % 5 == 0 and y>(x+0.5)):
    y = y - x - 0.5
    print('%.2f' % y)
else: 
    print('%.2f' % y)