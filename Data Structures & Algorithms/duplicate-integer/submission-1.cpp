class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> myset(begin(nums),end(nums));
        if (size(nums)>myset.size()){
            return true;
        }
        return false;
    }
};