import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if math.sqrt((x1-x2)**2 + (y1-y2)**2) == math.sqrt(5):
    print('True')
else:
    print('False')