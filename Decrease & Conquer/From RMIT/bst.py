import ascii_printer


class BST:
    EMPTY_TREE = -1

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Add key to tree.
        
        @param key
        """
        self.root = self.insert_from_root(self.root, key)

    def insert_from_root(self, root, key):
        """
        Recursive method to add key to tree.
        
        @param root Root node of tree to add 'key'.
        @param key Key to add to tree.
        @return Update root node.   
        """
        # check if root is empty
        if root is None:
            root = Node(key)
        elif key < root.key:
            root.left_child = self.insert_from_root(root.left_child, key)
        elif key > root.key:
            root.right_child = self.insert_from_root(root.right_child, key)

        return root

    def search(self, key):
        """
        Search for a key in the tree using binary search.
        
        @param key Key to search for.
        @return True if key is in the BST, otherwise false.
        """
        return self.search_from_root(self.root, key)

    def search_from_root(self, root, key):
        """
        Recursive method to search for a key in the tree using binary search.
        
        @param root Root node of the tree.
        @param key Key to search for.
        @return True if key is in the BST, otherwise false.
        """
        if root is None:
            return False
        elif root.key == key:
            return True
        elif key < root.key:
            return self.search_from_root(root.left_child, key)
        else:
            return self.search_from_root(root.right_child, key)

    def inorder(self):
        """
        Inorder traversal of tree.
        """
        self.inorder_from_root(self.root)
        print("")

    def inorder_from_root(self, root):
        if root is None:
            return

        self.inorder_from_root(root.left_child)
        print(f"{root.key} ", end="")
        self.inorder_from_root(root.right_child)

    def preorder(self):
        """
        preorder traversal of tree
        """
        self.preorder_from_root(self.root)
        print("")

    def preorder_from_root(self, root):
        """
        Preorder traversal of tree.
        
        @param root Root node of the tree.
        """
        if root is None:
            return

        print(f"{root.key} ", end="")
        self.preorder_from_root(root.left_child)
        self.preorder_from_root(root.right_child)

    def postorder(self):
        """
        Postorder traversal of tree.
        """
        self.postorder_from_root(self.root)
        print("")

    def postorder_from_root(self, root):
        """
        Postorder traversal of tree.
        
        @param root Root node of the tree.
        """
        if root is None:
            return

        self.postorder_from_root(root.left_child)
        self.postorder_from_root(root.right_child)
        # In general, might be better to use a function object here, but for this lab, we just print to stdout
        print(f"{root.key} ", end="")

    def ascii_print(self):
        """
        Print out tree in ascii text.
        """
        ascii_printer.print_node(self.root)

    def min(self):
        """
        Find minimum key in tree.

        @return Minimum key in tree.
        """
        # TO BE IMPLEMENTED
        if self.root is None:
            return -1
        return self.find_min(self, self.root)
    
    def find_min(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def max(self):
        """
        Find maximum key in tree.

        @return Maximum key in tree.
        """
        # TO BE IMPLEMENTED
        if self.root is None:
            return -1
        return self.find_max(self, self.root)
    
    def find_max(self, node):
        while node.right_child is not None:
            node = node.right_child
        return node

    def height(self):
        """
        Compute the height of the tree.
        @return Height of tree.
        """
        return self.height_from_root(self.root)
    
    def height_from_root(self, root):
        if root is None:
            return -1
        return 1 + max(self.height_from_root(root.left_child),
                       self.height_from_root(root.right_child))


class Node:
    def __init__(self, key):
        """

        @param key: Key to store in node.
        """
        # For this lab, we only store integers, but in general we can store any object/type that is Comparable.
        self.key = key
        # Reference to left child.
        self.left_child = None
        # Reference to right child.
        self.right_child = None

