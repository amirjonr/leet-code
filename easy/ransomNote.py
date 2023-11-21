def canConstruct(ransomNote: str, magazine: str) -> bool:
    dic = {}
    for i in magazine:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1

    # bounded by m
    for j in ransomNote:
        if j not in dic.keys():
            return False
        else:
            dic[j] -= 1
            if dic[j] < 0:
                return False

    return True


print(canConstruct('ryt', 'qwertyt'))
print(canConstruct('rytt', 'qwerty'))

# Time complexity O(m, cause m > n)
# Space complexity O(1), k <= 26 (lower letters in english = 26)
