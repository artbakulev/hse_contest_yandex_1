input()
numbers, N = list(map(int, input().split())), int(input())
curr_diff, curr = abs(numbers[0] - N), numbers[0]
for numb in numbers[1:]:
    if abs(N - numb) < curr_diff:
        curr_diff = abs(N - numb)
        curr = numb
print(curr)
