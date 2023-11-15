def plusOne(digits):
    return [int(i) for i in str(int(''.join([str(i) for i in [str(i) for i in digits]])) + 1)]


print(plusOne([8, 9, 9]))
print(plusOne([9, 9]))
print(plusOne([1, 0, 5]))
