# 297
class Codec:

    def serialize(self, root:TreeNode)->str:
        queue=collections.deque([root])
        result=['#']
        while queue:
            node=queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)




    def deserialize(self, data:str)->TreeNode:

        # 예외 처리 : 빈 이진 트리
        if data=='# #':
            return None

        nodes=data.split()

        root=TreeNode(int(nodes[1]))
        queue=collections.deque([root])
        index=2

        # 빠른 런너 처럼 자식 노드 결과를 먼저 확인 후 큐 삽입

        while queue:
            node=queue.popleft()
            if nodes[index] is not '#':
                node.left=TreeNode(int(nodes[index]))
                queue.append(node.left)
            index+=1
            if nodes[index] is not '#':
                node.right=TreeNode(int(nodes[index]))
                queue.append(node.right)
            index+=1
        return root
