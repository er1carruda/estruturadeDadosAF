class NodeTree:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return NodeTree(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search_rec(root.left, key)
        else:
            return self._search_rec(root.right, key)

    def inorder(self):
        self._inorder_rec(self.root)

    def _inorder_rec(self, root):
        if root:
            self._inorder_rec(root.left)
            print(root.key)
            self._inorder_rec(root.right)
