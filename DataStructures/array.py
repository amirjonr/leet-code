arr = [x for x in range(1, 11)]  # [1, 2, 3, .....9, 10]

arr.append(11)  # O(1)
print(arr)

arr.insert(0, 0)  # O(n)
print(arr)

arr.remove(11)  # O(n)
print(arr)

el = arr.pop()  # O(1)
print(arr)

value = arr.index(5)  # O(n)
print('value of index 5: ' + str(value))

count = len(arr)
print("count: " + str(count))

value = arr[0]  # 0(1)
print("Array's first element: " + str(value))

s = 0
n = int(input())
for i in range(1, n):  # 1 (1 .... n)
    s += i  # n
print(s)   # 1

# O(1 + n + 1) = O(n)

if 5 > 6:
    print(True)