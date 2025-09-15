/**
 * Problem: Two Sum
 * Difficulty: Easy
 * Date: 2025-09-14
 * Language: C++
 * Approach: Hash Map
 * Time: O(n)
 * Space: O(n)
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

class Solution {
public:
    /**
     * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
     * 
     * @param nums Array of integers
     * @param target Target sum
     * @return Indices of the two numbers that add up to target
     */
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            }
            map[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution solution;
    
    // Test cases
    struct TestCase {
        std::vector<int> nums;
        int target;
        std::vector<int> expected;
    };
    
    std::vector<TestCase> testCases = {
        {{2, 7, 11, 15}, 9, {0, 1}},
        {{3, 2, 4}, 6, {1, 2}},
        {{3, 3}, 6, {0, 1}},
    };
    
    for (size_t i = 0; i < testCases.size(); ++i) {
        auto result = solution.twoSum(testCases[i].nums, testCases[i].target);
        bool passed = (result == testCases[i].expected);
        
        std::cout << "Test " << (i + 1) << ": " << (passed ? "PASS" : "FAIL") << std::endl;
        std::cout << "  Input: nums=[";
        for (size_t j = 0; j < testCases[i].nums.size(); ++j) {
            std::cout << testCases[i].nums[j];
            if (j < testCases[i].nums.size() - 1) std::cout << ", ";
        }
        std::cout << "], target=" << testCases[i].target << std::endl;
        std::cout << "  Expected: [" << testCases[i].expected[0] << ", " << testCases[i].expected[1] << "]" << std::endl;
        std::cout << "  Got: [" << result[0] << ", " << result[1] << "]" << std::endl;
        std::cout << std::endl;
    }
    
    return 0;
}
