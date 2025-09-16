/*
Problem: Add Two Numbers
Difficulty: Medium
Date: 2025-09-15
Language: Rust
Approach: Iterative with carry
Time: O(max(m, n))
Space: O(max(m, n))
*/

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
    }
}

impl Solution {
    /// Add two numbers represented as linked lists where digits are stored in reverse order.
    /// 
    /// # Arguments
    /// * `l1` - First number as linked list
    /// * `l2` - Second number as linked list
    /// 
    /// # Returns
    /// Sum as linked list in reverse order
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut current = &mut dummy;
        let mut carry = 0;
        let mut l1 = l1;
        let mut l2 = l2;
        
        while l1.is_some() || l2.is_some() || carry > 0 {
            // Get values from current nodes (0 if node is None)
            let val1 = l1.as_ref().map_or(0, |node| node.val);
            let val2 = l2.as_ref().map_or(0, |node| node.val);
            
            // Calculate sum and new carry
            let total = val1 + val2 + carry;
            carry = total / 10;
            let digit = total % 10;
            
            // Create new node with the digit
            current.next = Some(Box::new(ListNode::new(digit)));
            current = current.next.as_mut().unwrap();
            
            // Move to next nodes if they exist
            l1 = l1.and_then(|node| node.next);
            l2 = l2.and_then(|node| node.next);
        }
        
        dummy.next
    }
}

pub struct Solution;

/// Helper function to create linked list from vector of digits
fn create_linked_list(digits: Vec<i32>) -> Option<Box<ListNode>> {
    if digits.is_empty() {
        return None;
    }
    
    let mut head = Box::new(ListNode::new(digits[0]));
    let mut current = &mut head;
    
    for &digit in digits.iter().skip(1) {
        current.next = Some(Box::new(ListNode::new(digit)));
        current = current.next.as_mut().unwrap();
    }
    
    Some(head)
}

/// Helper function to convert linked list to vector for easy comparison
fn linked_list_to_vec(head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut result = Vec::new();
    let mut current = head;
    
    while let Some(node) = current {
        result.push(node.val);
        current = node.next;
    }
    
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_two_numbers() {
        let test_cases = vec![
            (vec![2, 4, 3], vec![5, 6, 4], vec![7, 0, 8]), // 342 + 465 = 807
            (vec![0], vec![0], vec![0]),                     // 0 + 0 = 0
            (vec![9, 9, 9, 9, 9, 9, 9], vec![9, 9, 9, 9], vec![8, 9, 9, 9, 0, 0, 0, 1]), // 9999999 + 9999 = 10009998
        ];

        for (i, (l1_digits, l2_digits, expected)) in test_cases.iter().enumerate() {
            let l1 = create_linked_list(l1_digits.clone());
            let l2 = create_linked_list(l2_digits.clone());
            let result_head = Solution::add_two_numbers(l1, l2);
            let result = linked_list_to_vec(result_head);
            
            assert_eq!(result, *expected, "Test case {} failed", i + 1);
            println!("Test {}: PASS", i + 1);
            println!("  Input: l1={:?}, l2={:?}", l1_digits, l2_digits);
            println!("  Expected: {:?}", expected);
            println!("  Got: {:?}", result);
            println!();
        }
    }
}

fn main() {
    println!("Add Two Numbers - Rust Implementation");
    println!("=====================================");
    println!();
    
    let test_cases = vec![
        (vec![2, 4, 3], vec![5, 6, 4], vec![7, 0, 8]), // 342 + 465 = 807
        (vec![0], vec![0], vec![0]),                     // 0 + 0 = 0
        (vec![9, 9, 9, 9, 9, 9, 9], vec![9, 9, 9, 9], vec![8, 9, 9, 9, 0, 0, 0, 1]), // 9999999 + 9999 = 10009998
    ];

    for (i, (l1_digits, l2_digits, expected)) in test_cases.iter().enumerate() {
        let l1 = create_linked_list(l1_digits.clone());
        let l2 = create_linked_list(l2_digits.clone());
        let result_head = Solution::add_two_numbers(l1, l2);
        let result = linked_list_to_vec(result_head);
        
        let passed = result == *expected;
        println!("Test {}: {}", i + 1, if passed { "PASS" } else { "FAIL" });
        println!("  Input: l1={:?}, l2={:?}", l1_digits, l2_digits);
        println!("  Expected: {:?}", expected);
        println!("  Got: {:?}", result);
        println!();
    }
    
    println!("Run tests with: cargo test");
}
