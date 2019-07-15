/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *predecessor = head;
        ListNode *scout = head;
        for (int i = 0; i < n; i++) {
            if (scout->next == NULL) {
                return head->next;
            }
            scout = scout->next;
        }
        while (scout->next != NULL) {
            predecessor = predecessor->next;
            scout = scout->next;
        }
        predecessor->next = predecessor->next->next;
        return head;
    }
};