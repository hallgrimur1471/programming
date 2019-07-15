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
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *predecessor = dummy;
        ListNode *scout = dummy;
        for (int i = 0; i < n; i++) {
            scout = scout->next;
        }
        while (scout->next != NULL) {
            predecessor = predecessor->next;
            scout = scout->next;
        }
        predecessor->next = predecessor->next->next;
        return dummy->next;
    }
};