"""
Problem: Two Sum
Difficulty: Easy
Date: 2025-09-14
Language: Python
Approach: Hash Map
Time: O(n)
Space: O(n)
"""

def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
    
    Returns:
        List[int]: Indices of the two numbers that add up to target
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases):
        result = twoSum(nums, target)
        print(f"Test {i+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print()
