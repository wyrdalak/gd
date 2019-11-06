a = float(input())
b = float(input())
c = str(input())
if c == "+":
    s = b + a
    print(s)
elif c == "-":
    s = b - a
    print(s)
elif c == "/" and b != 0:
    s = b / a
    print(s)
elif c == "*":
    s = b * a
    print(s)
else:
    print("ЫЫЫЫЫЫ")