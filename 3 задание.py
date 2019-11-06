y = int(input())
x = int(input())
y1 = int(input())
x1 = int(input())
if (x + 5 == x1 or x - 5 == x1) and (y + 2 == y1 or y -2 == y1):
    print("YESSSS!")
elif (x + 2 == x1 or x - 2 == x1) and (y + 5 == y1 or y - 5 == y1):
    print("YESSSS!")
else:
    print("No no")