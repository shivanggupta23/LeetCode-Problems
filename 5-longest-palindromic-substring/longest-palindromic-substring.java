class Solution {
    public String longestPalindrome(String s) {
        int n=s.length();
        int start=0,maxLength=1;
        for(int i=0;i<n;i++){
            for(int j=0;j<=1;j++){
                int low=i;
                int high=i+j;

                while(low>=0 && high<n && s.charAt(low)==s.charAt(high)){
                    int currentLen=high-low+1;
                    if(currentLen>maxLength){
                        start=low;
                        maxLength=currentLen;
                    }
                    low--;
                    high++;
                }
            }
        }
        return s.substring(start,start+maxLength);
    }
}