def quicksort(arr, left, right):
    if left >= right:
        return

    p = partition(arr, left, right)
    quicksort(arr, left, p-1)
    quicksort(arr, p+1, right)

def partition(arr, left, right):
    pivot = arr[right]

    i = left-1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1

if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    quicksort(arr, 0, len(arr)-1)

    print(arr)
