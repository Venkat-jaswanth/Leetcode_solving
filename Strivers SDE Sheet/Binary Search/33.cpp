#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int search(vector<int>& arr, int target) {

        int n = arr.size() , low = 0, high = n-1;
        int pivot = 0;
        int mid = 0;
        while (low<=high){
            mid = (low + high) / 2;
            if ((mid == 0 || arr[mid] < arr[mid - 1]) &&
                (mid == n - 1 || arr[mid] < arr[mid + 1])) {
                pivot = mid;
                break;
            }
            if(arr[mid]>arr[n-1]){
                low = mid+1;
            }
            else{
                high = mid;
            }
        
        } 

        if(target <= arr[n-1]){
            low = pivot;
            high = n-1;
        }
        else{
            low = 0;
            high = pivot - 1;
        }

        while(low<=high){
            mid = (low+high) / 2;
            if(target == arr[mid]){
                return mid;
            }
            if (target>arr[mid]){
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }
        return -1;
    }
};
