from sympy.codegen.ast import continue_


def containsNearbyDuplicate(nums,  k: int) -> bool:
    charmap = {}
    for right in range(len(nums)):
        if nums[right] in charmap and (abs(charmap[nums[right]] - right)) <= k:
                return True
        charmap[nums[right]] = right

    return False

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))