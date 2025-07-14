#  O(n²) – Quadratic Time
# Two nested loops → time increases very fast.


def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(f"({i}, {j})")

# Test
print_all_pairs([1, 2, 3])


# For 3 elements → prints 9 pairs. For 100 → prints 10,000 pairs.