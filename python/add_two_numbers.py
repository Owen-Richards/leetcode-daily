"""
Problem: Add Two Numbers
Difficulty: Medium
Date: 2025-09-15
Language: Python
Approach: Iterative with carry
Time: O(max(m, n))
Space: O(max(m, n))
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """Helper method to display linked list"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return "[" + ",".join(result) + "]"

def addTwoNumbers(l1, l2):
    """
    Add two numbers represented as linked lists where digits are stored in reverse order.
    
    Args:
        l1 (ListNode): First number as linked list
        l2 (ListNode): Second number as linked list
    
    Returns:
        ListNode: Sum as linked list in reverse order
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values from current nodes (0 if node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and new carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node with the digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

def create_linked_list(digits):
    """Helper function to create linked list from list of digits"""
    if not digits:
        return None
    
    head = ListNode(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = ListNode(digit)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
        ([0], [0], [0]),                      # 0 + 0 = 0
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])  # 9999999 + 9999 = 10009998
    ]
    
    for i, (l1_digits, l2_digits, expected) in enumerate(test_cases):
        l1 = create_linked_list(l1_digits)
        l2 = create_linked_list(l2_digits)
        result_head = addTwoNumbers(l1, l2)
        result = linked_list_to_list(result_head)
        
        print(f"Test {i+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"  Input: l1={l1_digits}, l2={l2_digits}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        print()
