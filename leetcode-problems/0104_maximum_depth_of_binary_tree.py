"""
N: # nodes
Approach 1: Recursion
- O(# nodes), worst: O(# nodes), best: O(log(#nodes))

Approach 2: Tail Recursion + BFS
- O(N), T: O(N)

Approach 3: Iteration
- O(N), T: worst: O(N), best: O(log N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    # approach - 2
    """
    class Solution {
          private:
            // The queue that contains the next nodes to visit, 
            //   along with the level/depth that each node is located.
            queue<pair<TreeNode*, int>> next_items;
            int max_depth = 0;
            
            /**
             * A tail recursion function to calculate the max depth
             *   of the binary tree.
             */
            int next_maxDepth() {
            
              if (next_items.size() == 0) {
                return max_depth;
              }
                
              auto next_item = next_items.front();
              next_items.pop();
        
              auto next_node = next_item.first;
              auto next_level = next_item.second + 1;
              
              max_depth = max(max_depth, next_level);
        
              // Add the nodes to visit in the following recursive calls.
              if (next_node->left != NULL) {
                next_items.push(make_pair(next_node->left, next_level));
              }
              if (next_node->right != NULL) {
                next_items.push(make_pair(next_node->right, next_level));
              }
            
              // The last action should be the ONLY recursive call
              //   in the tail-recursion function.
              return next_maxDepth();
            }
            
          public:
            int maxDepth(TreeNode* root) {
              if (root == NULL) return 0;
                
              // clear the previous queue.
              std::queue<pair<TreeNode*, int>> empty;
              std::swap(next_items, empty);
              max_depth = 0;
                
              // push the root node into the queue to kick off the next visit.
              next_items.push(make_pair(root, 0));
                
              return next_maxDepth();
            }
        };
    """
    def maxDepth3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth

    def maxDepth(self, root):
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            node = queue.pop(0)
            depth += 1
            for _ in range(len(queue)):
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth