// Inorder, Preorder and Postorder tree traversal
#include <bits/stdc++.h> 
using namespace std; 

/* Here a binary tree node is created. It contains data (which is int), 
and pointer to left and right child */
struct Node 
{ 
	int data; 
	struct Node* left, *right; 
	Node(int data) 
	{ 
		this->data = data; 
		left = NULL; 
		right=NULL;
	} 
}; 

/*
The inorder traversal of a binary search tree involves visiting each
 of the nodes in the tree in the order (Left, Root, Right).

	Algorithm for  inorder traversal of tree using recursion 
	Inorder(tree)
   1. First traverse the left subtree, it means call Inorder(left->subtree)
   2. Then, visit the root.
   3. And then traverse the right subtree, which means call Inorder(right->subtree) 
*/

void inorder(struct Node* node) 
{ 
	if (node == NULL) 
		return; 

	/* Recursively call the left subtree */
	inorder(node->left); 

	/* Print the data of the node */
	cout << node->data << " "; 

	/* Recursively call the right subtree */
	inorder(node->right); 
} 

/*
The preorder traversal of a binary search tree involves visiting each
 of the nodes in the tree in the order ( Root,Left, Right).

	Algorithm for  preorder traversal of tree using recursion:
	
	Preorder(tree)
   1. First visit the root.
   2. Then, traverse the left subtree, it means call Preorder(left->subtree).
   3. And then traverse the right subtree, which means call Preorder(right->subtree).
 
 */
void preorder(struct Node* node) 
{ 
	if (node == NULL) 
		return; 

	/* Print the data of the node */
	cout << node->data << " "; 

	/* Recursively call the left subtree */
	preorder(node->left); 

	/* Recursively call the right subtree */
	preorder(node->right); 
} 


/*
The postorder traversal of a binary search tree involves visiting each
 of the nodes in the tree in the order (Left, Right, Root).
 
	Algorithm for  postorder traversal of tree using recursion:
	
	Postorder(tree)
   1. First traverse the left subtree, it means call Postorder(left->subtree)
   2. Then, traverse the right subtree, which means call Postorder(right->subtree)
   3. And then visit the root.
*/


void postorder(struct Node* node) 
{ 
	if (node == NULL) 
		return; 

	/* Recursively call the left subtree */
	postorder(node->left); 

	/* Recursively call the right subtree */
	postorder(node->right); 

	/* Print the data of the node */
	cout << node->data << " "; 
} 



/* Main function*/
int main() 
{ 
	/* Constructed a tree like this:
	     20
	    /  \
	  12	30
	 /  \   / \
	4   15 25  50
	
	*/
	struct Node *node = new Node(20); 
	node->left = new Node(12); 
	node->right	= new Node(30); 
	node->left->left = new Node(4); 
	node->left->right = new Node(15); 
	node->right->left = new Node(25); 
	node->right->right = new Node(50);
	
	//Doing inorder traversal of tree
	cout << "Inorder traversal is :\n"; 
	inorder(node); 
	
	//Doing preorder traversal of tree
	cout << "\n\nPreorder traversal is :\n"; 
	preorder(node); 
 
	//Doing postorder traversal of tree
	cout << "\n\nPostorder traversal is :\n"; 
	postorder(node); 

	return 0; 
} 

