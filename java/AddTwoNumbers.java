/**
 * Problem: Add Two Numbers
 * Difficulty: Medium
 * Date: 2025-09-15
 * Language: Java
 * Approach: Iterative with carry
 * Time: O(max(m, n))
 * Space: O(max(m, n))
 */

import java.util.*;

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    
    @Override
    public String toString() {
        List<Integer> result = new ArrayList<>();
        ListNode current = this;
        while (current != null) {
            result.add(current.val);
            current = current.next;
        }
        return result.toString();
    }
}

public class AddTwoNumbers {
    /**
     * Add two numbers represented as linked lists where digits are stored in reverse order.
     * 
     * @param l1 First number as linked list
     * @param l2 Second number as linked list
     * @return Sum as linked list in reverse order
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;
        
        while (l1 != null || l2 != null || carry != 0) {
            // Get values from current nodes (0 if node is null)
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;
            
            // Calculate sum and new carry
            int total = val1 + val2 + carry;
            carry = total / 10;
            int digit = total % 10;
            
            // Create new node with the digit
            current.next = new ListNode(digit);
            current = current.next;
            
            // Move to next nodes if they exist
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        
        return dummy.next;
    }
    
    /**
     * Helper method to create linked list from array of digits
     */
    public static ListNode createLinkedList(int[] digits) {
        if (digits == null || digits.length == 0) return null;
        
        ListNode head = new ListNode(digits[0]);
        ListNode current = head;
        
        for (int i = 1; i < digits.length; i++) {
            current.next = new ListNode(digits[i]);
            current = current.next;
        }
        
        return head;
    }
    
    /**
     * Helper method to convert linked list to array for easy comparison
     */
    public static int[] linkedListToArray(ListNode head) {
        List<Integer> result = new ArrayList<>();
        ListNode current = head;
        
        while (current != null) {
            result.add(current.val);
            current = current.next;
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
    
    public static void main(String[] args) {
        AddTwoNumbers solution = new AddTwoNumbers();
        
        // Test cases
        int[][][] testCases = {
            {{2, 4, 3}, {5, 6, 4}, {7, 0, 8}}, // 342 + 465 = 807
            {{0}, {0}, {0}},                    // 0 + 0 = 0
            {{9, 9, 9, 9, 9, 9, 9}, {9, 9, 9, 9}, {8, 9, 9, 9, 0, 0, 0, 1}} // 9999999 + 9999 = 10009998
        };
        
        for (int i = 0; i < testCases.length; i++) {
            int[] l1Digits = testCases[i][0];
            int[] l2Digits = testCases[i][1];
            int[] expected = testCases[i][2];
            
            ListNode l1 = createLinkedList(l1Digits);
            ListNode l2 = createLinkedList(l2Digits);
            ListNode resultHead = solution.addTwoNumbers(l1, l2);
            int[] result = linkedListToArray(resultHead);
            
            System.out.println("Test " + (i + 1) + ": " + 
                (Arrays.equals(result, expected) ? "PASS" : "FAIL"));
            System.out.println("  Input: l1=" + Arrays.toString(l1Digits) + 
                ", l2=" + Arrays.toString(l2Digits));
            System.out.println("  Expected: " + Arrays.toString(expected));
            System.out.println("  Got: " + Arrays.toString(result));
            System.out.println();
        }
    }
}
