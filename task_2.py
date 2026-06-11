"""
Longest contiguous subsequence with sum equal to zero.

Algorithm: prefix sums + dictionary.
If prefix_sum[i] == prefix_sum[j] for i < j,
then the subarray s[i+1..j] sums to zero.
We track the first occurrence of each prefix sum to maximize length.

Time complexity:  O(n)
Space complexity: O(n)
"""


def longest_subsequence(s):
    """
    Return the length of the longest contiguous subsequence of s
    whose elements sum to zero.

    Parameters
    ----------
    s : list of int
        Input sequence. The original list is not modified.

    Returns
    -------
    int
        Length l (0 <= l <= n) of the longest zero-sum subarray.
    """
    first_seen = {0: -1}

    prefix_sum = 0
    best_length = 0

    for i, value in enumerate(s):
        prefix_sum += value

        if prefix_sum in first_seen:
            length = i - first_seen[prefix_sum]
            if length > best_length:
                best_length = length
        else:
            first_seen[prefix_sum] = i

    return best_length

if __name__ == "__main__":
    s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print("s1 result:", longest_subsequence(s1), " (expected 0)")

    s2 = [100, 5, 0, -5, 1, 1, 1, 1, 1, -5, -5, 5, 5, 5, -3, -7, 7, 25, -15, -7, -3, -5, -21, 38]
    print("s2 result:", longest_subsequence(s2), " (expected 16)")

    print("empty list:", longest_subsequence([]),          " (expected 0)")
    print("single 0 :", longest_subsequence([0]),          " (expected 1)")
    print("single 1 :", longest_subsequence([1]),          " (expected 0)")
    print("[1, -1]  :", longest_subsequence([1, -1]),      " (expected 2)")
    print("[0, 0, 0]:", longest_subsequence([0, 0, 0]),    " (expected 3)")
    print("[1,2,-3,4,-4]:", longest_subsequence([1,2,-3,4,-4]), " (expected 5)")

    original = [1, -1, 2]
    _ = longest_subsequence(original)
    assert original == [1, -1, 2], "Input list was modified!"
    print("Input list unchanged: OK")

    import time
    import random
    random.seed(42)
    big = [random.randint(-100, 100) for _ in range(15_000)]
    start = time.perf_counter()
    result = longest_subsequence(big)
    elapsed = time.perf_counter() - start
    print(f"\nPerformance test (n=15000): length={result}, time={elapsed:.4f}s")