#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution{
public:
    struct compare{
        bool operator()(ListNode* a,ListNode* b){
            return a->val > b->val;
        }
    };
    ListNode* mergeKLists(vector<ListNode*>& lists){
        priority_queue<ListNode*,vector<ListNode*>,compare> pq;
        for(auto l : lists){
            if(l)pq.push(l);
        }
        ListNode* dummy = new ListNode(-1);
        ListNode* tail = dummy;


        while(!pq.empty()){
            ListNode* current = pq.top();
            pq.pop();
            tail->next = current;
            tail = tail->next;
            if(current->next){
                pq.push(current->next);
            }
        }
        return dummy->next;
    }

};