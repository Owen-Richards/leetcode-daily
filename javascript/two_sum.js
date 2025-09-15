/**
 * Problem: Two Sum
 * Difficulty: Easy
 * Date: 2025-09-14
 * Language: JavaScript
 * Approach: Hash Map
 * Time: O(n)
 * Space: O(n)
 */

/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * @param {number[]} nums - Array of integers
 * @param {number} target - Target sum
 * @return {number[]} Indices of the two numbers that add up to target
 */
var twoSum = function(nums, target) {
    const map = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
};

// Test cases
const testCases = [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]],
];

testCases.forEach((testCase, index) => {
    const [nums, target, expected] = testCase;
    const result = twoSum(nums, target);
    console.log(`Test ${index + 1}: ${JSON.stringify(result) === JSON.stringify(expected) ? 'PASS' : 'FAIL'}`);
    console.log(`  Input: nums=${JSON.stringify(nums)}, target=${target}`);
    console.log(`  Expected: ${JSON.stringify(expected)}`);
    console.log(`  Got: ${JSON.stringify(result)}`);
    console.log();
});
