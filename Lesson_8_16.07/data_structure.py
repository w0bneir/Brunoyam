# # def array():
# #     l=[1,5.9, "123"]
# #     print(l[1])
# #     l[1] = "qwe"
# #     print(l[1])
# #     l.append(123)
# #     l.pop(len(l)-1)
# #     l.insert(1, 456)
# #     l.pop(1)
# #     print(l)
# # array()
# # import array
# array
# srt
# frozenset
# stack
# deque
# queue
# dict
# map
# hashtable
# ordereddict
# chain
class Node:
    def __init__(self, info, left, right):
        self.info = info
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.info)

    def horizontal(self, root):
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            print(node.info, [str(x) for x in list(queue)])

    def preorder(self, root):
        if root is None:
            return
        print(root.info)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.info)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.info)


def init_tree():
    f = Node("F")
    g = Node("G")
    e = Node("E")
    d = Node("D", f, g)
    c = Node("C", e)
    b = Node("B", right=d)
    a = Node("A", b, c)


root = init_tree()
