maxes = [int(input()), int(input())]
if maxes[0] < maxes[1]:
    maxes.reverse()

while True:
    number = int(input())
    if number == 0:
        break
    if number > maxes[0]:
        maxes[1] = maxes[0]
        maxes[0] = number
    elif number > maxes[1]:
        maxes[1] = number
print(maxes[1])
