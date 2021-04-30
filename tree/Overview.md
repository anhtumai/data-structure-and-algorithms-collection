# Tree

A tree whose elements have at most 2 children is binary tree.

## Binary Search Tree

Compared to list, it is faster to insert and remove in BST.
It is usefull since in real-life application, data constantly updates.

Definition: a BST is a binary tree which values of left sub-tree <= root <= right sub-tree. There must be no dupplicated nodes.


| Operation | (Sorted) List | BST         |
| --------- | ------------- | ----------- |
| Search    | O(log(n))     | O(log(n))   |
| Insert    | O(n)          | O(log(n))   |
| Remove    | O(n)          | O(log(n))   |