#include <unordered_map>
#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // Step 1: build next greater map for nums2
        unordered_map<int, int> nextGreater;
        stack<int> st; // stores values

        for (int val : nums2) {
            while (!st.empty() && st.top() < val) {
                nextGreater[st.top()] = val;
                st.pop();
            }
            st.push(val);
        }

        while (!st.empty()) {
            nextGreater[st.top()] = -1;
            st.pop();
        }

        // Step 2: lookup
        vector<int> result;
        for (int x : nums1)
            result.push_back(nextGreater[x]);

        return result;
    }
};
