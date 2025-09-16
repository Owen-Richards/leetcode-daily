# Add Two Numbers
**Difficulty:** Medium  
**Date:** 2025-09-15  
**LeetCode Link:** https://leetcode.com/problems/add-two-numbers/

## Problem Statement
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Examples
**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998
```

### Constraints
- The number of nodes in each linked list is in the range `[1, 100]`
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros

## Approaches

### Approach 1: Naive Conversion
**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(max(m, n))

Convert linked lists to integers, add them, then convert back to linked list. However, this approach can cause integer overflow for large numbers.

#### Implementation Notes
- Risk of integer overflow with large numbers
- Requires additional conversion steps
- Not optimal for this problem structure

### Approach 2: Iterative with Carry (Optimized)
**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(max(m, n))

Traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous addition. This mimics elementary addition by hand.

#### Implementation Notes
- Handle different list lengths gracefully
- Maintain carry for digits that sum > 9
- Continue until both lists are exhausted AND carry is 0
- Use dummy head to simplify edge cases

#### Algorithm Steps
1. Initialize dummy head and current pointer
2. Initialize carry to 0
3. While either list has nodes OR carry > 0:
   - Get values from current nodes (0 if null)
   - Calculate sum = val1 + val2 + carry
   - Update carry = sum // 10
   - Create new node with digit = sum % 10
   - Move pointers forward
4. Return dummy.next

## Edge Cases
- Different length linked lists (e.g., [1,8] + [0])
- Carry at the end (e.g., [5] + [5] = [0,1])
- Single digit numbers (e.g., [0] + [0])
- Maximum length lists with carries

## Key Learnings
- **Linked list traversal** with multiple pointers
- **Carry handling** in arithmetic operations
- **Dummy head technique** simplifies linked list problems
- **Simultaneous iteration** over multiple data structures
- **Edge case handling** for different input sizes

## Related Problems
- [Multiply Strings](https://leetcode.com/problems/multiply-strings/)
- [Add Strings](https://leetcode.com/problems/add-strings/)
- [Plus One](https://leetcode.com/problems/plus-one/)
- [Add Binary](https://leetcode.com/problems/add-binary/)

## Languages Completed
- [x] Python
- [x] JavaScript
- [x] Java
- [ ] C++
- [ ] Rust
