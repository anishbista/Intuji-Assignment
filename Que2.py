# Find a pair with the given sum in an array. Given an unsorted integer array, print a pair
# with the given sum in it.

nums = [5, 2, 8, 1, 7, 3, 4, 6]
target = int(input("Enter the target: "))
pair = []

for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pair.append((nums[i], nums[j]))

print(f"Pair that sums of target: {pair}")
