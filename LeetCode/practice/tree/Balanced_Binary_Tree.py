#110

# 트리의 높이에 관한 문제이므로, dfs를 활용해서 bottom up으로 backtracking하면서 높이를 갱신해간다.
# My Solution : Recursive

class Solution:
    Flag:bool=True

    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node:TreeNode)->int:

            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            if abs(left-right)>=2:
                self.Flag=False

            return max(left,right)+1

        dfs(root)

        return self.Flag
      
 # Book Solution : Recursive     
