queen = (int(input()), int(input()))
chessman = (int(input()), int(input()))

if queen[0] == chessman[0]:
    print("YES")
elif queen[1] == chessman[1]:
    print("YES")
elif abs(queen[0] - chessman[0]) == abs(queen[1] - chessman[1]):
    print("YES")
else:
    print("NO")
