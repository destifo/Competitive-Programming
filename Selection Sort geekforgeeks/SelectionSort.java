
/**
https://practice.geeksforgeeks.org/problems/selection-sort/1#
**/

public class SelectionSort{

    int select(int[]arr, int i){
        return arr[i];
    }

    void selectionSort(int[]arr, int n){
        for (int i = 0; i < n; i++){
            int minIndex = i;
            for (int j = n - 1; j >= i;j-- ){
                if (arr[j] < arr[minIndex])
                    minIndex = j;
            }
            int temp = select(arr, minIndex);
            arr[minIndex] = arr[i];
            arr[i] = temp;

        }
    }
}