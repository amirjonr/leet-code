def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)



print(strStr('mississippi', 'issip'))