


# ALGORITHMS WITH C/C++
## Introduction
algorithms research created by Non Weerawong Vonggatunyu or Qu1etboy
the language use to writing this is C++
## C++ Syntax
Basic syntax use in this research
### Input/Output
```c++
int x; // declare a variable
cin >> x // take input 
cout << x // print x
```
### If-Else
```c++
if (condition1) {
	// do something
} else if (condition2) {
	// do something
} else {
	// do something
}
```
or writing in short form
``result = (condition) ? true : false;``
### While
```c++
while (condition) {
	// do something
}
```
### For-loop
```c++
//   initilize  condition increment
for (int i = 0; i < 5; i++) {
	// do something
}
```
##  Searching
### Linear Search
loop through array if the element is equal to target return the position otherwise return -1 
time complexity is $`O(n)`$
```c++
int linearSearch(int arr[], int target, int n) {
	for (int i =  0; i < n; i++) {
		if (arr[i] == target) {
			return i;
		}
	}
	return -1;
}
```
### Binary Search
using **divide and Conquer** approach
find the middle element in array compare to target cut array in half if a middle element is less than target
search the right side otherwise search the left side
time complexity is $`O(logn)`$
```c++
int binarySearch(int arr[], int target, int n) {
	int left = 0, right = n - 1;
	while (left <= right) {
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
}
```
##  Sorting
Sorting  with time complexity if $`O(n^2)`$
### Bubble sort
```c++
for (int i = 0; i < n; i++)
	for (int j = 0; j < n - 1; j++)
		if (arr[j] > arr[j + 1])
			swap(arr[j], arr[j + 1]);
```
### Selection sort
loop through array find the smallest element and swap with the first element of array do it until everything sorted
```c++
for (int i = 0; i < n; i++)
	for (int j = i + 1; j < n; j++)
		if (arr[i] > arr[j])
			swap(arr[i], arr[j]);
```
### Insertion sort
Sorting with time complexity of $`O(nlogn)`$
**Merge sort**
**Quick sort**

## Complete Search
### Find all Subset
- Recursive
```cpp
vector<vector<int>> ans;
vector<int> res;

void genSubset(int k) {
	if (k == n) {
		ans.push_back(res);
		return;
	}
	res.push_back(arr[k]);
	genSubset(k + 1);
	res.pop_back();
	genSubset(k + 1);
}
```
- Iteration (bitmask)
```cpp
vector<vector<int>> ans;
for (int bit = 0; bit < (1 << n); bit++) {
	vector<int> res;
	for (int j = 0; j < n; j++) {
		if (bit & (1 << j)) {
			res.push_back(arr[j])
		}
	}
	ans.push_back(res);
}
```
### Find all Permutation
- Recursive
```cpp
int chosen[INF]; // INF = max length
vector<vector<int>> ans;
vector<int> res;

void permute(int k) {
	if (k == n) {
	    ans.push_back(res);
		return;
	}
	for (int i = 0; i < n; i++) {
		if (chosen[i]) continue;
		res.push_back(arr[i]);
		chosen[i] = 1;
		permute(k + 1);
		res.pop_back();
		chosen[i] = 0;
	}
}
```
## Implementation
Common algorithm or problems that have seen most in computer science

**Remove element in array**
```c++
void removeElement(int arr[], int element_to_remove, int n) {
	int j = 0;
	for (int i  = 0; i < n; i++)
		if (arr[j] != element_to_remove)
			arr[j++] = arr[i];
	arr[j] = 0; 
}
```
**Valid Palindrome**
```c++
int isPalindrome(string s, int n) {
	int left = 0, right = n - 1
	while (left < right) {
		if (s[left++] != s[right--])
			return 0;
	}
	return 1;
}
```
**Anagram**
Anagram is a word that come from rearranging the other word
easily check is s1 is anagram of s2 by sorting both of the string and check if a character is equal or not 
```c++
int isAnagram(string s1, string s2) {
	sort(s1);
	sort(s2);
	for (int i = 0; i < strlength; i++) 
		if (s1 != s2)
			return 0;
	return 1;
}
```
**Maximum Subarray Sum**
```c++
int maximumSubArraySum(int arr[], int n) {
	int ans = arr[i], sum = 0;
	for (int i = 0; i < n; i++) {
		sum = max(sum + arr[i], arr[i]);
		ans = max(ans, sum);
	}
	return ans;
} 
```
another version of this problem in https://beta.programming.in.th/tasks/1005
```c++
#include <iostream> 
using namespace std; 
int main() { 
	int n; 
	cin >> n; 
	int a[n]; 
	for (int i = 0; i < n; i++) 
		cin >> a[i]; 
	int sum = 0, ans = a[0], start = 0, curr_start = 0, end = 0; 
	for (int i = 0; i < n; i++) { 
		if (sum + a[i] > 0) { 
			sum += a[i]; 
		} 
		else { 
			sum = 0; 
			curr_start = i + 1; 
		} 
		if (sum > ans) { 
			ans = sum; 
			start = curr_start; 
			end = i; 
		} 
	} 
	if (ans <= 0) { 
		cout << "Empty sequence" << '\n'; 
		return 0; 
	} 
	for (int i = start; i < end + 1; i++) 
		cout << a[i] << " "; cout << '\n' << ans; 
	return 0; 
}
```

