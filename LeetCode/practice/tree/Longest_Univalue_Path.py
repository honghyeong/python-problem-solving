    def longestUnivaluePath(self, root: TreeNode) -> int:

        def dfs(node:TreeNode)->int:

            if node is None:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            if node.left and node.left.val==node.val: # null node ( 존재하지않는 노드의 val을 가져오려 한 오류가 생긴다. )
                left+=1
            else:
                left=0
            if node.right and node.right.val==node.val: # null node ( 존재하지않는 노드의 val을 가져오려 한 오류가 생긴다. )
                right+=1
            else:
                right=0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최대값이 결과
            self.longest=max(self.longest,left+right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left,right)
        dfs(root)

        return self.longest
