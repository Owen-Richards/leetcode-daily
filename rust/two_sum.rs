/*
Problem: Two Sum
Difficulty: Easy
Date: 2025-09-14
Language: Rust
Approach: Hash Map
Time: O(n)
Space: O(n)
*/

use std::collections::HashMap;

impl Solution {
    /// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    /// 
    /// # Arguments
    /// * `nums` - A vector of integers
    /// * `target` - Target sum
    /// 
    /// # Returns
    /// A vector containing indices of the two numbers that add up to target
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&index) = map.get(&complement) {
                return vec![index as i32, i as i32];
            }
            map.insert(num, i);
        }
        vec![]
    }
}

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_sum() {
        let test_cases = vec![
            (vec![2, 7, 11, 15], 9, vec![0, 1]),
            (vec![3, 2, 4], 6, vec![1, 2]),
            (vec![3, 3], 6, vec![0, 1]),
        ];

        for (i, (nums, target, expected)) in test_cases.iter().enumerate() {
            let result = Solution::two_sum(nums.clone(), *target);
            assert_eq!(result, *expected, "Test case {} failed", i + 1);
            println!("Test {}: PASS", i + 1);
            println!("  Input: nums={:?}, target={}", nums, target);
            println!("  Expected: {:?}", expected);
            println!("  Got: {:?}", result);
            println!();
        }
    }
}

fn main() {
    println!("Run tests with: cargo test");
}
