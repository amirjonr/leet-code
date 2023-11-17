def numberOfSteps(self, num: int) -> int:
    k = 0
    while num != 0:
        k += 1
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
    return k
