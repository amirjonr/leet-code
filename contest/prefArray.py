def calculate_prefix_similarity(arr1, arr2):
    prefix_similarity = 0
    min_len = min(len(arr1), len(arr2))

    for i in range(min_len):
        if arr1[i] == arr2[i]:
            prefix_similarity += 1
        else:
            break

    return prefix_similarity


def pairwise_similarity_sum(arrays):
    n = len(arrays)
    total_similarity = 0

    for i in range(n):
        for j in range(i + 1, n):
            total_similarity += calculate_prefix_similarity(arrays[i], arrays[j])

    return total_similarity


with open('input.txt', 'r') as file:
    n = int(file.readline())
    arrays = []

    for _ in range(n):
        k = int(file.readline())
        array = list(map(int, file.readline().split()))
        arrays.append(array)

result = pairwise_similarity_sum(arrays)

with open('output.txt', 'w') as file:
    file.write(f"{result}\n")
