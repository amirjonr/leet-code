import os


# first solution
def common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):
        current_string = strs[i]
        j = 0

        mini = min(len(prefix), len(current_string))
        while j < mini and prefix[j] == current_string[j]:
            j += 1

        prefix = prefix[:j]

        if not prefix:
            break

    return prefix


# Example usage:
array_of_strings = ["flower", "flow", "flight"]


result = common_prefix(array_of_strings)
print(result)


# second solution
def common_prefix(strings):
    if not strings:
        return ""

    # Using os.path.commonprefix to find the common prefix
    prefix = os.path.commonprefix(strings)

    return prefix


# Example usage:
array_of_strings = ["flower", "flow", "flight"]
result = common_prefix(array_of_strings)
print(result)

