# ---------- Brute Force ----------
# Time: O(n^2)
# Space: O(1)

def contains_duplicate_bruteforce(nums):

    n = len(nums)

    for i in range(n):

        for j in range(i + 1, n):

            if nums[i] == nums[j]:
                return True

    return False


# ---------- Optimised (Set) ----------
# Time: O(n)
# Space: O(n)

def contains_duplicate_optimised(nums):

    seen = set()

    for x in nums:

        if x in seen:
            return True

        seen.add(x)

    return False


if __name__ == "__main__":

    nums = [1, 2, 3, 1]

    print("Brute:", contains_duplicate_bruteforce(nums))
    print("Optimised:", contains_duplicate_optimised(nums))