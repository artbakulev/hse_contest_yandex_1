N = int(input())
numbers = input().split(' ')
for i in range(N):
    numbers[i] = int(numbers[i])
N = int(input())
nearest = numbers[0]
diff = abs(N - numbers[0])

for i in range(1, len(numbers)):
    t_diff = abs(N - numbers[i])
    if t_diff < diff:
        nearest = numbers[i]
        diff = t_diff
print(nearest)
