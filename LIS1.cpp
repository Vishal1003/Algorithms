int lengthOfLIS(vector<int>& nums) {
        
        
        
        //O(n*n) solution
        int ans=0; int arr[10000];
        for(int i=0;i<nums.size();i++) arr[i]=1;
        vector<int> temp;
        for(int i=1;i<nums.size();i++)
        {
            for(int j=0;j<i;j++)
                if(nums[j]<nums[i]) arr[i]=max(arr[i],arr[j]+1);
        }
        for(int i=0;i<nums.size();i++)  ans=max(ans,arr[i]);
        return ans; 
}
