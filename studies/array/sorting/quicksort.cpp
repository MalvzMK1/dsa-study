#include <iostream>

void printArray(int* arr, int n) {
  for (int i = 0; i < n; i++) {
    std::cout << arr[i] << ", ";
  }
  
  std::cout << std::endl;
}

int partition(int* arr, int left, int right) {
  int pivot = arr[right];

  int i = left-1;

  for (int j = left; j < right; j++) {
    if (arr[j] <= pivot) {
      i += 1;
      int tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
  }

  int tmp = arr[i+1];
  arr[i+1] = arr[right];
  arr[right] = tmp;

  return i+1;
}

void quicksort(int* arr, int left, int right) {
  if (left >= right) return;

  int p = partition(arr, left, right);
  quicksort(arr, left, p-1);
  quicksort(arr, p+1, right);
}

int main() {
  int arr[] {9, 8, 7, 6, 5, 4, 3, 2, 1};
  int size = sizeof(arr) / sizeof(arr[0]);

  printArray(arr, size);
  quicksort(arr, 0, size-1);
  printArray(arr, size);

  return 0;
}
