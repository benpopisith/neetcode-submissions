class Solution {
    public int[] replaceElements(int[] arr) {
        // we want to look at the elements right of i
        for (int i = 0; i < arr.length; i++) {
            int greatest = 0;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] > greatest) {
                    greatest = arr[j];
                }
            }
            arr[i] = greatest;
        }
        arr[arr.length - 1] = -1;
        return arr;
    }
}