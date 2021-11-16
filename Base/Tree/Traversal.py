# Cause tree is self-defined recursive structure, so recursive algorithm works well, good to see

def preOrder(node):
    if node is None:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node):
    if node is None:
        return
    
    preOrder(node.left)
    print(node.val)
    preOrder(node.right)

    
def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.val)
    
