first, second, current = int(input()), int(input()), int(input())
if first < second:
    first, second = second, first
while current != 0:
    if current > first:
        first, second = current, first
    elif current > second:
        second = current
    current = int(input())
print(second)
