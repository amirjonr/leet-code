import timeit


class BinaryTree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def pretty_print(self, prefix="", is_left=True):
        if self.right:
            self.right.pretty_print(prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(self.root))
        if self.left:
            self.left.pretty_print(prefix + ("    " if is_left else "│   "), True)

    def search(self, key):
        if self.root is None or self.root == key:
            return self
        if key < self.root:
            return self.left.search(key) if self.left else None
        return self.right.search(key) if self.right else None


def measure_search_time(tree, key):
    start_time = timeit.default_timer()
    result = tree.search(key)
    end_time = timeit.default_timer()
    return result, end_time - start_time


def create_balanced_tree(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = BinaryTree(mid + 1)
    root.left = create_balanced_tree(start, mid - 1)
    root.right = create_balanced_tree(mid + 1, end)
    return root


# Creating a balanced binary search tree
balanced_tree = create_balanced_tree(0, 19)

print("Balanced Binary Search Tree:")
balanced_tree.pretty_print()

# Example usage of the search function with measurement
key_to_search = 15
result, search_time = measure_search_time(balanced_tree, key_to_search)

if result:
    print(f"\nKey {key_to_search} found in the tree.")
else:
    print(f"\nKey {key_to_search} not found in the tree.")

print(f"Search time: {search_time} seconds")


class LinearSearchArray:
    def __init__(self, array):
        self.array = array
        self.operations = 0

    def search(self, key):
        # Linear search for a key in the array
        for index, value in enumerate(self.array):
            self.operations += 1
            if value == key:
                return index
        return -1


def measure_linear_search_time(linear_search_array, key):
    start_time = timeit.default_timer()
    result = linear_search_array.search(key)
    end_time = timeit.default_timer()
    return result, end_time - start_time, linear_search_array.operations


# Creating an array for linear search
linear_search_array = list(range(20))

print("Array for Linear Search:")
print(linear_search_array)

# Example usage of linear search with measurement
key_to_search_linear = 15
linear_search_result, linear_search_time, linear_search_operations = measure_linear_search_time(
    LinearSearchArray(linear_search_array), key_to_search_linear
)

if linear_search_result != -1:
    print(f"\nKey {key_to_search_linear} found at index {linear_search_result} using linear search.")
else:
    print(f"\nKey {key_to_search_linear} not found in the array using linear search.")

print(f"Number of operations for linear search: {linear_search_operations}")
print(f"Linear search time: {linear_search_time} seconds")
