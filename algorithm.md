


# ALGORITHMS WITH C/C++
## Introduction
algorithms research created by Non Weerawong Vonggatunyu or Qu1etboy
the language use to writing this is C++

##  Searching
**Linear Search**
loop through array if the element is equal to target return the position otherwise return -1 
time complexity is $O(n)$
```c++
int arr[n] = {1, 2, 3 ,4 ,5}, target = 3;
for (int i =  0; i < n; i++) {
	if (arr[i] == target) {
		return i;
	}
}
return -1;
```
**Binary Search**
find the middle element in array compare to target cut array in half if a middle element is less than target
search the right side otherwise search the left side
time complexity is $O(logn)$
```c++
int arr[] = {1, 2, 3, 4, 5}, target = 4;
int left = 0, right = n - 1;
while (left < right) {
	int mid = (left + right) / 2;
	if (arr[mid] == target) {
		return mid;
	}
	else if (arr[mid] > target) {
		right = mid - 1;
	}
	else {
		left = mid + 1;
	}
}
```
##  Sorting
Sorting  with time complexity if $O(n^2)$
**Bubble sort**
```c++
for (int i = 0; i < n; i++)
	for (int j = 0; j < n - 1; j++)
		if (arr[j] > arr[j + 1])
			swap(arr[j], arr[j + 1]);
```
**Selection sort**
loop through array find the smallest element and swap with the first element of array do it until everything sorted
```c++
for (int i = 0; i < n; i++)
	for (int j = i + 1; j < n; j++)
		if (arr[i] > arr[j])
			swap(arr[i], arr[j]);
```
**Insertion sort**
Sorting with time complexity of $O(nlogn)$
**Merge sort**
**Quick sort**

## Implementation
Common algorithm or problems that have seen most in computer science

**Remove element in array**
```c++
int j = 0;
for (int i  = 0; i < n; i++)
	if (arr[j] != element_to_remove)
		arr[j++] = arr[i];
arr[j] = 0; 
```
**Valid Palindrome**
**Anagram**
**Maximum Subarray**
