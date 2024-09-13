def min_steps_to_equal(a, b):
    diff = abs(a - b)
    steps = 0

    for k in range(10, 0, -1):
        steps += diff // k
        diff %= k

    return steps

a, b = map(int, input().split())
result = min_steps_to_equal(a, b)
print(result)
