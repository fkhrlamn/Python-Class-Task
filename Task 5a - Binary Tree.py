#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Task 5a - Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printPreorder(node):
    if node:
        print(node.data, end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printInorder(node):
    if node:
        printInorder(node.left)
        print("-->",node.data, end=" ")
        printInorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print("-->",node.data, end=" ")

root = Node(2)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.right.left = Node(6)
root.left.right = Node(4)
root.left.right.left = Node(5)
root.right.right = Node(8)
printPreorder(root)
print()
printInorder(root)
print()
printPostorder(root)
