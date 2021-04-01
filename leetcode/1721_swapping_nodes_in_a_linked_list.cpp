/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        int n = 1;
        ListNode* tmp = head;
        while (tmp->next != NULL) {
            tmp = tmp->next;
            n++;
        }
        
        if (k > n/2) {
            k = n-k+1;
        }
        
        if (k == (n-(k-1)) || n == 1) {
            return head;
        }
        else {
            ListNode* p1 = head;
            ListNode* p2 = head;
            ListNode* p1_prev = NULL;
            ListNode* p2_prev = NULL;
            for (int i = 0; i < k-1; i++) {
                p1_prev = p1;
                p1 = p1->next;
            }
            for (int i = 0; i < (n - k); i++) {
                p2_prev = p2;
                p2 = p2->next;
            }

            if ((n-k) == k) {
                p1->next = p2->next;
                p2->next = p1;
            }
            else {
                tmp = p1->next;
                p1->next = p2->next;
                p2->next = tmp;
            }
            
            if (p2_prev != p1) {
                p2_prev->next = p1;
            }
            if (p1_prev != NULL) {
                p1_prev->next = p2;
            }
            
            if (k == 1) {
                return p2;
            }
            else {
                return head;
            }
        }
    }
};
