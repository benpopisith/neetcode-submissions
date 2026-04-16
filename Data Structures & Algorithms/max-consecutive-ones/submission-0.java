class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int longestStreak = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                count++;
                if (count > longestStreak) {
                    longestStreak = count;
                }
            }
            else {
                count = 0;
            }
        }
        return longestStreak;
    }
}