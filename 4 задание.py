x, y = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
x5, y5 = map(int, input().split())
x6, y6 = map(int, input().split())
x7, y7 = map(int, input().split())
x8, y8 = map(int, input().split())
if ((x != x2 or x3 or x4 or x5 or x6 or x7 or x8) or (x2 != x or x3 or x4 or x5 or x6 or x7 or x8) or (x3 != x or x2 or x4 or x5 or x6 or x7 or x8) or (x4 != x or x2 or x3 or x5 or x6 or x7 or x8) or (x5!= x or x2 or x3 or x4 or x6 or x7 or x8) or (x6 != x or x2 or x3 or x4 or x5 or x7 or x8) or (x7 != x or x2 or x3 or x4 or x5 or x6 or x8) or (x8 == x or x2 or x3 or x4 or x5 or x6 or x7) and ((y != y2 or y3 or y4 or y5 or y6 or y7 or y8) or (y2 != y or y3 or y4 or y5 or y6 or y7 or y8) or (y3 != y or y2 or y4 or y5 or y6 or y7 or y8) or (y4 != y or y2 or y3 or y5 or y6 or y7 or y8) or (y5!= y or y2 or y3 or y4 or y6 or y7 or y8) or (y6 != y or y2 or y3 or y4 or y5 or y7 or y8) or (y7 != y or y2 or y3 or y4 or y5 or y6 or y8) or (y8 != y or y2 or y3 or y4 or y5 or y6 or y7))):
    if (x < (x2 or x3 or x4 or x5 or x6 or x7 or x8) and y < (y2 or y3 or y4 or y5 or y6 or y7 or y8)) and (x - y == ((x2 - y2) or (x3 - y3) or (x4 - y4) or (x5- y5) or (x6 - y6) or (x7 - y7) or (x8 - y8))):
        print("YES")
    elif (x < (x2 or x3 or x4 or x5 or x6 or x7 or x8) and y > (y2 or y3 or y4 or y5 or y6 or y7 or y8)) and (x + y == ((x2 + y2) or (x3 + y3) or (x4 + y4) or (x5 + y5) or (x6 + y6) or (x7 + y7) or (x8 + y8))):
        print("YES")
    elif (x > (x2 or x3 or x4 or x5 or x6 or x7 or x8) and y > (y2 or y3 or y4 or y5 or y6 or y7 or y8)) and (x - y == ((x2 - y2) or (x3 - y3) or (x4 - y4) or (x5- y5) or (x6 - y6) or (x7 - y7) or (x8 - y8))):
        print("YES")
    elif (x > (x2 or x3 or x4 or x5 or x6 or x7 or x8) and y < (y2 or y3 or y4 or y5 or y6 or y7 or y8)) and (x + y == ((x2 + y2) or (x3 + y3) or (x4 + y4) or (x5 + y5) or (x6 + y6) or (x7 + y7) or (x8 + y8))):
        print("YES")
    else:
        print("NO")
elif ((x == x2 or x3 or x4 or x5 or x6 or x7 or x8) or (x2 == x or x3 or x4 or x5 or x6 or x7 or x8) or (x3 == x or x2 or x4 or x5 or x6 or x7 or x8) or (x4 == x or x2 or x3 or x5 or x6 or x7 or x8) or (x5== x or x2 or x3 or x4 or x6 or x7 or x8) (x6 == x or x2 or x3 or x4 or x5 or x7 or x8) or (x7 == x or x2 or x3 or x4 or x5 or x6 or x8) or (x8 == x or x2 or x3 or x4 or x5 or x6 or x7)and ((y == y2 or y3 or y4 or y5 or y6 or y7 or y8) or (y2 == y or y3 or y4 or y5 or y6 or y7 or y8) or (y3 == y or y2 or y4 or y5 or y6 or y7 or y8) or (y4 == y or y2 or y3 or y5 or y6 or y7 or y8) or (y5 == y or y2 or y3 or y4 or y6 or y7 or y8) or (y6 == y or y2 or y3 or y4 or y5 or y7 or y8) or (y7 == y or y2 or y3 or y4 or y5 or y6 or y8) or (y8 == y or y2 or y3 or y4 or y5 or y6 or y7))):
    print("YES")
else:
    print("NO")

