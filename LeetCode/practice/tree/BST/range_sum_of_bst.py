# 938

# Recursive Brute Force Search : DFS
class Solution:
    result:int=0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def dfs(root:TreeNode):
            if root:
                if root.val<=high and root.val>=low:
                    self.result+=root.val
                dfs(root.left)
                dfs(root.right)
        

        dfs(root)
        return self.result

# + Pruning : DFS
class Solution:
    result:int=0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def dfs(node:TreeNode):
            if not node:
                return 0

            if node.val<low:
                return dfs(node.right)  ## BST 특성상 왼쪽 dfs는 더 작은 값들이므로 볼 필요가 없어서 pruning
            elif node.val>high:
                return dfs(node.left)    ## BST 특성상 오른쪽 dfs는 더 큰 값들이므로 볼 필요가 없어서 pruning

            return node.val + dfs(node.left)+dfs(node.right)

        return dfs(root)
    
# Iteration DFS    

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        stack=[root]
        sum=0
        while stack:
            node=stack.pop()
            if node:
                if low>node.val:
                    stack.append(node.right)
                elif high<node.val:
                    stack.append(node.left)
                else:
                    sum+=node.val
                    stack.append(node.left)
                    stack.append(node.right)

        return sum

# Iteration BFS

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        queue=collections.deque([root])
        sum=0
        while queue:
            node=queue.popleft()
            if node:
                if node.val>low:
                    queue.append(node.left)
                if node.val<high:
                    queue.append(node.right)
                if low<=node.val<=high:
                    sum+=node.val
            return sum



    
