# Two Sum
**Difficulty:** Easy  
**Date:** 2025-09-14  
**LeetCode Link:** https://leetcode.com/problems/two-sum/

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Approaches

### Approach 1: Brute Force
**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

The brute force approach checks every pair of numbers to see if they sum to the target. For each element, we check every other element to see if they add up to the target.

#### Implementation Notes
- Nested loops: outer loop for first element, inner loop for second element
- Simple but inefficient for large arrays

### Approach 2: Hash Map (Optimized)
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use a hash map to store numbers we've seen and their indices. For each number, check if its complement (target - current number) exists in the hash map.

#### Implementation Notes
- Single pass through the array
- Hash map lookup is O(1) on average
- Store number as key, index as value

## Edge Cases
- Array with exactly 2 elements
- Negative numbers in the array
- Target is 0
- Duplicate numbers that sum to target

## Key Learnings
- Hash maps provide O(1) average lookup time
- Trading space for time complexity is often worthwhile
- Always consider the complement when looking for pairs
- One-pass solutions are often more elegant than two-pass

## Related Problems
- [3Sum](https://leetcode.com/problems/3sum/)
- [4Sum](https://leetcode.com/problems/4sum/)
- [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Languages Completed
- [x] Python
- [x] JavaScript
- [x] Java
- [x] C++
- [x] Rust
