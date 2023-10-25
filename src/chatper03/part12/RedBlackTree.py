# 定义红黑树节点类
class Node:
    def __init__(self, key, parent=None, color="RED"):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color

NIL_LEAF = Node(None, color="BLACK")

# 定义红黑树类
class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = NIL_LEAF
        self.root = NIL_LEAF

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        current = self.root
        parent = None

        while current is not self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.color == "RED" and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)

            if node == self.root:
                break
        self.root.color = "BLACK"

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        if current_node is not self.NIL_LEAF:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.key)
            self._inorder_recursive(current_node.right, result)

# 测试红黑树
rb_tree = RedBlackTree()
keys = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]

for key in keys:
    rb_tree.insert(key)

print(rb_tree.inorder_traversal())  # 输出排序后的节点值列表
