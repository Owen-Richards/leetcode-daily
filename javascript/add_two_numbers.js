/**
 * Problem: Add Two Numbers
 * Difficulty: Medium
 * Date: 2025-09-15
 * Language: JavaScript
 * Approach: Iterative with carry
 * Time: O(max(m, n))
 * Space: O(max(m, n))
 */

/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val);
    this.next = (next===undefined ? null : next);
}

/**
 * Add two numbers represented as linked lists where digits are stored in reverse order.
 * @param {ListNode} l1 - First number as linked list
 * @param {ListNode} l2 - Second number as linked list
 * @return {ListNode} Sum as linked list in reverse order
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;
    
    while (l1 || l2 || carry) {
        // Get values from current nodes (0 if node is null)
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;
        
        // Calculate sum and new carry
        const total = val1 + val2 + carry;
        carry = Math.floor(total / 10);
        const digit = total % 10;
        
        // Create new node with the digit
        current.next = new ListNode(digit);
        current = current.next;
        
        // Move to next nodes if they exist
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }
    
    return dummy.next;
};

/**
 * Helper function to create linked list from array of digits
 */
function createLinkedList(digits) {
    if (!digits || digits.length === 0) return null;
    
    let head = new ListNode(digits[0]);
    let current = head;
    
    for (let i = 1; i < digits.length; i++) {
        current.next = new ListNode(digits[i]);
        current = current.next;
    }
    
    return head;
}

/**
 * Helper function to convert linked list to array for easy comparison
 */
function linkedListToArray(head) {
    const result = [];
    let current = head;
    
    while (current) {
        result.push(current.val);
        current = current.next;
    }
    
    return result;
}

// Test cases
const testCases = [
    [[2, 4, 3], [5, 6, 4], [7, 0, 8]], // 342 + 465 = 807
    [[0], [0], [0]],                     // 0 + 0 = 0
    [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]] // 9999999 + 9999 = 10009998
];

testCases.forEach((testCase, index) => {
    const [l1Digits, l2Digits, expected] = testCase;
    const l1 = createLinkedList(l1Digits);
    const l2 = createLinkedList(l2Digits);
    const resultHead = addTwoNumbers(l1, l2);
    const result = linkedListToArray(resultHead);
    
    console.log(`Test ${index + 1}: ${JSON.stringify(result) === JSON.stringify(expected) ? 'PASS' : 'FAIL'}`);
    console.log(`  Input: l1=${JSON.stringify(l1Digits)}, l2=${JSON.stringify(l2Digits)}`);
    console.log(`  Expected: ${JSON.stringify(expected)}`);
    console.log(`  Got: ${JSON.stringify(result)}`);
    console.log();
});
