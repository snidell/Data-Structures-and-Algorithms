1.) Sorting can help provide a more efficient Solution by making searching
faster
2.) Poor sorting algorithms can run in poor time O(N^2) like Bubblesort
3.) Better sorts run in 0(nlog(n)) time like heapsort, mergesort, and quicksort
Unstable sorts:
A sorting algorithm is said to be stable if two objects with equal keys appear
in the same order in the sorted output as they appear in the unsorted input.

Whereas a sorting algorithm is said to be unstable if there are two or more
objects with equal keys which don’t appear in same order before and after
sorting.

In-place sorts:
Use no additional memory to sort. They sort on the structure itself


Algo:          InPlace:                Stable:
Quicksort          Yes                   No
Mergesort          No                    Yes
Heapsort           Yes                   No

When does quicksort go bad ? When it consistently picks a poor pivot number
if sorting in ascending order and the pivot is pick with the lowest number
each iteration would be N-1,N-2...N-i for each sort leaving to O(n^2)

[10,7,8,6,3,12,14,2] --> pick 2
[2,10,7,8,6,3,12,14] --> pick 3
[2,3,10,7,8,6,12,14] --> pick 6
[2,3,6,10,7,8,12,14] --> pick... 
