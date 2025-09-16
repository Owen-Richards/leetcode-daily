/**
 * Problem: Add Two Numbers
 * Difficulty: Medium
 * Date: 2025-09-15
 * Language: C++
 * Approach: Iterative with carry
 * Time: O(max(m, n))
 * Space: O(max(m, n))
 */

#include <iostream>
#include <vector>
#include <cassert>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    /**
     * Add two numbers represented as linked lists where digits are stored in reverse order.
     * 
     * @param l1 First number as linked list
     * @param l2 Second number as linked list
     * @return Sum as linked list in reverse order
     */
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        int carry = 0;
        
        while (l1 || l2 || carry) {
            // Get values from current nodes (0 if node is nullptr)
            int val1 = l1 ? l1->val : 0;
            int val2 = l2 ? l2->val : 0;
            
            // Calculate sum and new carry
            int total = val1 + val2 + carry;
            carry = total / 10;
            int digit = total % 10;
            
            // Create new node with the digit
            current->next = new ListNode(digit);
            current = current->next;
            
            // Move to next nodes if they exist
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};

/**
 * Helper function to create linked list from vector of digits
 */
ListNode* createLinkedList(const std::vector<int>& digits) {
    if (digits.empty()) return nullptr;
    
    ListNode* head = new ListNode(digits[0]);
    ListNode* current = head;
    
    for (size_t i = 1; i < digits.size(); ++i) {
        current->next = new ListNode(digits[i]);
        current = current->next;
    }
    
    return head;
}

/**
 * Helper function to convert linked list to vector for easy comparison
 */
std::vector<int> linkedListToVector(ListNode* head) {
    std::vector<int> result;
    ListNode* current = head;
    
    while (current) {
        result.push_back(current->val);
        current = current->next;
    }
    
    return result;
}

/**
 * Helper function to delete linked list and free memory
 */
void deleteLinkedList(ListNode* head) {
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

/**
 * Helper function to print vector
 */
void printVector(const std::vector<int>& vec) {
    std::cout << "[";
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i];
        if (i < vec.size() - 1) std::cout << ",";
    }
    std::cout << "]";
}

int main() {
    Solution solution;
    
    // Test cases
    struct TestCase {
        std::vector<int> l1_digits;
        std::vector<int> l2_digits;
        std::vector<int> expected;
    };
    
    std::vector<TestCase> testCases = {
        {{2, 4, 3}, {5, 6, 4}, {7, 0, 8}}, // 342 + 465 = 807
        {{0}, {0}, {0}},                    // 0 + 0 = 0
        {{9, 9, 9, 9, 9, 9, 9}, {9, 9, 9, 9}, {8, 9, 9, 9, 0, 0, 0, 1}} // 9999999 + 9999 = 10009998
    };
    
    for (size_t i = 0; i < testCases.size(); ++i) {
        ListNode* l1 = createLinkedList(testCases[i].l1_digits);
        ListNode* l2 = createLinkedList(testCases[i].l2_digits);
        ListNode* resultHead = solution.addTwoNumbers(l1, l2);
        std::vector<int> result = linkedListToVector(resultHead);
        
        bool passed = (result == testCases[i].expected);
        
        std::cout << "Test " << (i + 1) << ": " << (passed ? "PASS" : "FAIL") << std::endl;
        std::cout << "  Input: l1=";
        printVector(testCases[i].l1_digits);
        std::cout << ", l2=";
        printVector(testCases[i].l2_digits);
        std::cout << std::endl;
        std::cout << "  Expected: ";
        printVector(testCases[i].expected);
        std::cout << std::endl;
        std::cout << "  Got: ";
        printVector(result);
        std::cout << std::endl << std::endl;
        
        // Clean up memory
        deleteLinkedList(l1);
        deleteLinkedList(l2);
        deleteLinkedList(resultHead);
    }
    
    return 0;
}
