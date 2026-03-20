# ---------- Brute Force ----------
# Time: O(n^2)
# Space: O(1)

def two_sum_bruteforce(nums, target):

    n = len(nums)

    for i in range(n):

        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# ---------- Optimised (HashMap) ----------
# Time: O(n)
# Space: O(n)

def two_sum_optimised(nums, target):

    mp = {}

    for i, x in enumerate(nums):
        diff = target - x
        if diff in mp:
            return [mp[diff], i]

        mp[x] = i

    return []


if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    print("Brute:", two_sum_bruteforce(nums, target))
    print("Optimised:", two_sum_optimised(nums, target))