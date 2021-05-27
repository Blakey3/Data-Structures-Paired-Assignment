#Assignment 3 2021 Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)
    """
    # Return the size of the tree
    def getSize(self):
      return self.size"""

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")

    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)

    
    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root

class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None

def menu():

    print('Please select an option below:')
    print('1. Print the pre-order, in-order, and post-order of the BST, in sequence')
    print('2. Print all leaf nodes of the BST, and all non-leaf nodes (seperately)')
    print('3. Print all the total number of nodes of a sub-tree')
    print('4. Print the depth of a subtree rooted at a particular node')
    print('5. Insert a new integer key into the BST')
    print('6. Delete an integer key from the BST')
    print('7. Exit')

    decision = int(input('Selection: '))

    if decision == 1:
        #preorder, postorder, in order
         print("\nPreorder traversal:")
        intTree.preorder()
        print("\n\nInorder traversal:")
        intTree.inorder()
        print("\n\nPostorder traversal:")
        intTree.postorder()
        menu()
    elif decision == 2:
        #leaf nodes
    elif decision == 3:
        #total number of nodes
    elif decision == 4:

    elif decision == 5:

    elif decision == 6:

    elif decision == 7:
          exit()

    else:

        print('Invalid input try again')
