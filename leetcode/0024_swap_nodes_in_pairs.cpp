#include <bits/stdc++.h>
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
    ListNode* swapPairs(ListNode* head) {
      if (head == NULL) {
        return NULL;
      }
      if (head->next == NULL) {
        return head;
      }
      ListNode* odd = head;
      ListNode* even = head->next;
      ListNode* new_head = even;
      while ((even->next != NULL) && (even->next->next != NULL)) {
        ListNode* next_odd = odd->next->next;
        ListNode* next_even = even->next->next;
        even->next = odd;
        odd->next = next_even;
        odd = next_odd;
        even = next_even;
      }
      if (even->next != NULL) {
        odd->next = even->next;
        even->next = odd;
      }
      else {
        even->next = odd;
        odd->next = NULL;
      }
      return new_head;
    }
};
