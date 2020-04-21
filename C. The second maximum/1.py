first_max = int(input())
second_max = int(input())
if first_max < second_max:
    t = first_max
    first_max = second_max
    second_max = t
while True:
    number = int(input())
    if number == 0:
        break
    if number > first_max:
        t = first_max
        first_max = number
        second_max = t
    elif number > second_max:
        second_max = number
print(second_max)
