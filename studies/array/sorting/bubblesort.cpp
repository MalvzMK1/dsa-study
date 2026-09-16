#include <iostream>

void printArray(int* arr, int n) {
  for (int i = 0; i < n; i++) {
    std::cout << arr[i] << ", ";
  }
  
  std::cout << std::endl;
}

void bubbleSort(int* arr, int n) {
  for (int i = 0; i < n-1; i++) {
    // printArray(arr, n);
    bool isSorted = true;
    for (int j = 0; j < n-1; j++) {
      if (arr[j] > arr[j+1]) {
        isSorted = false;
        int tmp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tmp;
      }
    }
    if (isSorted) return;
  }
}

// time complexity: O(n^2)
// space complexity: O(1)
int main() {
  // int arr[] {1, 2, 3, 4, 5}; // best case
  int arr[] {5, 4, 3, 2, 1}; // worst case
  int n = sizeof(arr) / sizeof(arr[0]);

  printArray(arr, n);
  bubbleSort(arr, n);
  printArray(arr, n);

  return 0;
}
