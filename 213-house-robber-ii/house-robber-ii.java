class Solution {
    public int rob(int[] nums) {
        int n=nums.length;
        if(n<2) return nums[0];
        int[] firstRob=new int[n-1];
        int[] lastRob=new int[n-1];
        for(int i=0;i<n-1;i++){
            firstRob[i]=nums[i];
            lastRob[i]=nums[i+1];
        }
        int firstResult=robResult(firstRob);
        int lastResult=robResult(lastRob);
        return Math.max(firstResult,lastResult);
    }
    public int robResult(int[] arr){
        if(arr.length<2) return arr[0];
        int[] dp=new int[arr.length];
        dp[0]=arr[0];
        dp[1]=Math.max(arr[0],arr[1]);
        for(int i=2;i<arr.length;i++){
            dp[i]=Math.max(dp[i-2]+arr[i],dp[i-1]);
        }
        return dp[arr.length-1];
    }
}