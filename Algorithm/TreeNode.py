class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6, TreeNode(7), TreeNode(8)))


def pre_order(root):
    if root == None:
        return "The is NuLL"
    print(root.data, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if root == None:
        return "The is NuLL"
    in_order(root.left)
    print(root.data,end= ' ')
    in_order(root.right)


def bac_order(root):
    if root == None:
        return "The is NuLL"
    bac_order(root.left)
    bac_order(root.right)
    print(root.data,  end=' ')


def BFS(root):
    if root is None:
        return
    queue = []
    vals = []
    queue.append(root)
    while queue:
        currentNode = queue.pop(0)
        vals.append(currentNode.data)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    for i in vals:
        print(i, end=' ')


def DFS(root):
    if root is None:
        return
    Stack = []
    vals = []
    Stack.append(root)
    while Stack:
        current = Stack.pop()
        vals.append(current.data)
        if current.right:
            Stack.append(current.right)
        if current.left:
            Stack.append(current.left)

    for i in vals:
        print(i, end=' ')


def MaxDepth(root):
    if root is None:
        return 0
    root_l =root.left
    root_r = root.right
    return max(MaxDepth(root_l), MaxDepth(root_r))+1



root1 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8),TreeNode(9)), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print("前序遍历：", end='')
pre_order(root1)
print('')
print("中序遍历：", end='')
in_order(root1)
print('')
print("后序遍历：", end='')
bac_order(root1)
print('')
print("广度遍历：", end='')
BFS(root1)
print('')
print("深度遍历：",end='')
DFS(root1)
print('')
print('最大树深:',MaxDepth(root1),end='')
