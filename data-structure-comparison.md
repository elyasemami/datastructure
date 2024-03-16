| Big O Notation | Description                             | Efficiency          | Example Algorithms                   | Notes                                                        |
|----------------|-----------------------------------------|---------------------|--------------------------------------|--------------------------------------------------------------|
| O(1)           | Constant Time                           | Most Efficient      | Accessing array element by index     | Time to complete doesn't change with the size of the input. |
| O(log N)       | Logarithmic Time                        | Highly Efficient    | Binary Search                        | Increases slowly as N grows. Ideal for searching/sorting.   |
| O(N)           | Linear Time                             | Efficient           | Linear Search                        | Time to complete increases linearly with the size of input. |
| O(N log N)     | Linearithmic Time                       | Moderately Efficient | Merge Sort, Quick Sort               | More efficient than quadratic for large N.                  |
| O(N^2)         | Quadratic Time                          | Less Efficient      | Bubble Sort, Insertion Sort          | Time to complete increases quadratically with input size.   |
| O(N^3)         | Cubic Time                              | Inefficient         | Naive matrix multiplication          | Practical only for small N.                                  |
| O(2^N)         | Exponential Time                        | Highly Inefficient  | Brute-force solutions for NP problems| Time to complete doubles with each additional element.      |
| O(N!)          | Factorial Time                          | Least Efficient     | Solving the Travelling Salesman Problem via brute-force | Impractical for even small sizes of N.                    |








| Data Structure       | Description                                                                 | Insert/Add    | Remove/Delete | Find/Peek | Access (Random access) | Notes                                                                                   |
|----------------------|-----------------------------------------------------------------------------|---------------|---------------|-----------|------------------------|-----------------------------------------------------------------------------------------|
| Binary Heap          | A complete binary tree where each node is smaller (min-heap) or larger (max-heap) than its children. | O(log n)      | O(log n)      | O(1)      | N/A                    | Used for priority queues; does not support random access.                               |
| Heap                 | A specialized tree-based data structure that satisfies the heap property.   | O(log n)      | O(log n)      | O(1)      | N/A                    | General term that includes binary heaps, binomial heaps, etc.                           |
| Tree                 | A hierarchical structure with a root value and subtrees of children with a parent node. | Varies        | Varies        | Varies    | N/A                    | Performance depends on specific type of tree (e.g., binary search tree, AVL tree).       |
| Stack                | A linear data structure which follows a particular order (LIFO).             | O(1)          | O(1)          | O(1)      | N/A                    | Ideal for backtracking, syntax parsing, etc.                                            |
| Queue                | A linear data structure which follows a particular order (FIFO).             | O(1)          | O(1)          | O(1)      | N/A                    | Useful in scheduling, buffering, etc.                                                   |
| Priority Queue       | An abstract data type similar to a regular queue or stack but where additionally, each element has a "priority" associated with it. | O(log n)   | O(log n)      | O(1)      | N/A                    | Implemented typically using heaps for efficient access to the highest or lowest element.|
| ArrayList            | A resizable array, which can grow as needed.                                | O(1) amortized | O(n)         | N/A       | O(1)                   | Provides random access, but removing elements requires shifting.                        |
| List (Interface)     | An ordered collection (also known as a sequence).                           | Varies        | Varies        | Varies    | Varies                 | Abstract type; performance depends on the implementing class (e.g., ArrayList, LinkedList). |
| LinkedList           | Consists of elements where each element has a reference to the next and previous element. | O(1)          | O(1)          | N/A       | O(n)                   | Faster insert and remove compared to ArrayList, but slower random access.               |




## Algos for trees and heaps:

### Binary Tree

A Binary Tree is a data structure where each node has at most two children, referred to as the left child and the right child. It is a specialized form of a tree where every node has zero, one, or two children.

### Simple Binary Tree Algorithm (Traversal)

#### In-Order Traversal (Recursive)
```java
void inOrderTraversal(Node node) {
    if (node == null)
        return;
    inOrderTraversal(node.left);
    System.out.print(node.data + " ");
    inOrderTraversal(node.right);
}


void heapify(int arr[], int n, int i) {
    int smallest = i; // Initialize smallest as root
    int l = 2*i + 1; // left = 2*i + 1
    int r = 2*i + 2; // right = 2*i + 2

    // If left child is smaller than root
    if (l < n && arr[l] < arr[smallest])
        smallest = l;

    // If right child is smaller than smallest so far
    if (r < n && arr[r] < arr[smallest])
        smallest = r;

    // If smallest is not root
    if (smallest != i) {
        int swap = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = swap;

        // Recursively heapify the affected sub-tree
        heapify(arr, n, smallest);
    }
}




| Algorithm      | Best Case Time Complexity | Average Case Time Complexity | Worst Case Time Complexity | Space Complexity | In-place | Stable | Remarks |
|----------------|---------------------------|------------------------------|----------------------------|------------------|----------|--------|---------|
| Heap Sort      | O(n log n)                | O(n log n)                   | O(n log n)                 | O(1)             | Yes      | No     | Heap sort builds a heap from the input data and then repeatedly extracts the maximum element from the heap and rebuilds the heap. |
| Merge Sort     | O(n log n)                | O(n log n)                   | O(n log n)                 | O(n)             | No       | Yes    | Merge sort divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. |
| Quicksort      | O(n log n)                | O(n log n)                   | O(n^2)                     | O(log n)         | Yes      | No     | Quicksort picks an element as pivot and partitions the given array around the picked pivot. The choice of pivot affects the performance. |
| Radix Sort     | O(nk)                     | O(nk)                        | O(nk)                      | O(n + k)         | No       | Yes    | Radix sort sorts the input array digit by digit, starting from the least significant digit to the most significant digit. `k` is the number of digits in the max value. |
| Insertion Sort | O(n)                      | O(n^2)                       | O(n^2)                     | O(1)             | Yes      | Yes    | Insertion sort works by taking elements from the unsorted list and inserting them at their correct position into a new sorted list. |
| Bubble Sort    | O(n)                      | O(n^2)                       | O(n^2)                     | O(1)             | Yes      | Yes    | Bubble Sort works by repeatedly swapping the adjacent elements if they are in wrong order. This algorithm is known for its simplicity but is inefficient for large lists. |

