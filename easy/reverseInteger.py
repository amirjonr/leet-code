def reverse(x):
    INT_MAX = 2 ** 31
    INT_MIN = -2 ** 31
    sign = 1 if x >= 0 else -1
    x *= sign
    x = int(str(x)[::-1])
    if x not in range(INT_MIN, INT_MAX):
        return 0
    else:
        return x * sign


print(reverse(1534236469))
print(reverse(-754))
