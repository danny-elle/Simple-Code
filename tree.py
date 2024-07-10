
class Node:
    # defines a Node and its branched leaf nodes 
    # self is the node
    # data is the value of that node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    # searchs the nodes to find the target node
    def search(self, target):
        if self.data == target:
            print("FOund it!")
            return self
        # is the target on the left of the tree
        if self.left and self.data > target:
            # recursively checks the left side of tree
            return self.left.search(target)
        # if the right exists and its less than target 
        if self.right and self.data < target:
            # recursivley search the right side of the tree
            return self.right.search(target)
        # invisible none statement if none of the conditiions were met
        print("Value is not in tree")


    # height of a tree
    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)



    # preorder goes left as much as it can until it goes right
    def traversePreorder(self):
        # print current node
        print(self.data)
        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()

    # prints nodes out from smallest to largest
    def traverseInorder(self):
        
        # preorder goes left (smallest node values)  as much as it can until it goes right
        if self.left:
            self.left.traversePreorder()

        # print current node
        print(self.data)

        if self.right:
            self.right.traversePreorder()
    
    # goes from left node to right up to parent node 
    def traversePostorder(self):
        
        # preorder goes left as much as it can until it goes right
        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()

        # print current node
        print(self.data)


#wrapper class node Tree
class Tree:

    # creates a tree node with a name
    def __init__(self, root, name=''):
        self.root = root
        self.name = name
    
    # searches the named node tree for a specific target
    def search(self, target):
        return self.root.search(target)
    
    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

# creates the root node
node = Node(10)
# creates the leaf child nodes of the root node
node.left = Node(5)
node.right = Node(15)
# creates the extended leaf child nodes of the child nodes
node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

print(node.right.data)
print(node.right.right.data)
# cr3eates a new named node tree
myTree = Tree(node, 'RYan\'s Tree')

print(myTree.name)
print(myTree.root.left.data)

print(myTree.root.right.right.data)

#found = myTree.root.search(10000)
found = myTree.search(10000)
print(found.data)

tree = Tree(Node(50), 'Tree Traversals')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)


print('Traverse Pre-Order')
tree.traversePreorder()

print('\nTraverse In-Order')
tree.traverseInorder()

print('\nTraverse Post-Order')
tree.traversePostorder()

print('\n')
print(tree.root.height())

ptree = Tree(Node(50), 'a very short tree')
print(ptree.root.height())
