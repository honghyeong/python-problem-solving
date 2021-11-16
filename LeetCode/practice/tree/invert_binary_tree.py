# Pythonic way, Recursive solution

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root
        return None

# Iteration, BFS

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue=collections.deque([root])

        while queue:
            node=queue.popleft()
            # 부모노트 부터 하향식 스왑
            if node:
                node.left,node.right=node.right,node.left

                queue.append(node.left)
                queue.append(node.right)
        return root

# Iteration, DFS

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack=collections.deque([root])

        while stack:
            node=stack.pop()
            
            if node:
                node.left,node.right=node.right,node.left
                
                stack.append(node.left)
                stack.append(node.right)

            # 부모 노드부터 하향식 스왑 (top - bottom)
        return root
 
  
 # Iteration, DFS 후위순회 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack=collections.deque([root])

        while stack:
            node=stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left,node.right=node.right,node.left # DFS 후위 순회
            # 부모 노드부터 하향식 스왑
        return root
