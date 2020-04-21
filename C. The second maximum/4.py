first = int(input())
second = int(input())
if first < second:
    first, second = second, first

current = int(input())
while current != 0:
    if current > first:
        second = first
        first = current
    elif current > second:
        second = current
    current = int(input())
print(second)
