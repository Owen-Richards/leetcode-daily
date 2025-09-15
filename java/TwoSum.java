/**
 * Problem: Two Sum
 * Difficulty: Easy
 * Date: 2025-09-14
 * Language: Java
 * Approach: Hash Map
 * Time: O(n)
 * Space: O(n)
 */

import java.util.*;

public class TwoSum {
    /**
     * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
     * 
     * @param nums Array of integers
     * @param target Target sum
     * @return Indices of the two numbers that add up to target
     */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
    
    public static void main(String[] args) {
        TwoSum solution = new TwoSum();
        
        // Test cases
        int[][][] testCases = {
            {{2, 7, 11, 15}, {9}, {0, 1}},
            {{3, 2, 4}, {6}, {1, 2}},
            {{3, 3}, {6}, {0, 1}},
        };
        
        for (int i = 0; i < testCases.length; i++) {
            int[] nums = testCases[i][0];
            int target = testCases[i][1][0];
            int[] expected = testCases[i][2];
            int[] result = solution.twoSum(nums, target);
            
            System.out.println("Test " + (i + 1) + ": " + 
                (Arrays.equals(result, expected) ? "PASS" : "FAIL"));
            System.out.println("  Input: nums=" + Arrays.toString(nums) + ", target=" + target);
            System.out.println("  Expected: " + Arrays.toString(expected));
            System.out.println("  Got: " + Arrays.toString(result));
            System.out.println();
        }
    }
}
