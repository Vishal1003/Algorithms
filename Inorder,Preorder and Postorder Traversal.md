1. Tree is a hierarchical data structure which stores the information naturally in the form of hierarchy style.
2. Tree is one of the most powerful and advanced data structures.
3. It is a non-linear data structure compared to arrays, linked lists, stack and queue.
4. It represents the nodes connected by edges.

The inorder traversal of a binary search tree involves visiting each
 of the nodes in the tree in the order (Left, Root, Right).

Algorithm for  inorder traversal of tree using recursion:
 
Inorder(tree)
   1. First traverse the left subtree, it means call Inorder(left->subtree)
   2. Then, visit the root.
   3. And then traverse the right subtree, which means call Inorder(right->subtree) 



The postorder traversal of a binary search tree involves visiting each
 of the nodes in the tree in the order (Left, Right, Root).
 
	Algorithm for  postorder traversal of tree using recursion:
	
	Postorder(tree)
   1. First traverse the left subtree, it means call Postorder(left->subtree)
   2. Then, traverse the right subtree, which means call Postorder(right->subtree)
   3. And then visit the root.


The preorder traversal of a binary search tree involves visiting each
 of the nodes in the tree in the order ( Root,Left, Right).

	Algorithm for  preorder traversal of tree using recursion:
	
	Preorder(tree)
   1. First visit the root.
   2. Then, traverse the left subtree, it means call Preorder(left->subtree).
   3. And then traverse the right subtree, which means call Preorder(right->subtree).

Time Complexity: O(n)