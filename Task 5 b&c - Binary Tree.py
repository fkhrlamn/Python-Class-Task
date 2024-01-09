# Initialize global variables
depth = 1
deepestPath = ""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def deepestBranch(self):
        findBranch(self)
        print("Deepest Branch Depth:", depth)
        print("Deepest Branch Path:", deepestPath)      

def insertSort(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insertSort(root.left, data)
        else:
            root.right = insertSort(root.right, data)
    return root

def printPreorder(root):
    if root:
        print("-->",root.data, end=' ')
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root):
    if root:
        printInorder(root.left)
        print("-->",root.data, end=' ')
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print("-->",root.data, end=' ')

def findBranch(root, currentdepth = 1, path = 'root'):
    global depth
    global deepestPath

    if root:
        # Update the depth and path if current depth is greater than the stored depth
        if currentdepth > depth:
            depth = currentdepth
            deepestPath = path

        findBranch(root.left, currentdepth + 1, path + " Left")
        findBranch(root.right, currentdepth + 1, path + " Right")

# depth and deepestPath are global variables
# node, root,left,right, currentdepth, path is the parameters
        


root = Node('Haziman Sairin')
insertSort(root, 'Zikri Hakim')
insertSort(root, 'Jameel Majdi')
insertSort(root, 'Raniya Waleed')
insertSort(root, 'Syukri Talib')
insertSort(root, 'Izzat Syahmi')
insertSort(root, 'Saif al-Din')
insertSort(root, 'Nuqman Aliff')
insertSort(root, 'Amir Su\'ad')
insertSort(root, 'Abdul Karim')
insertSort(root, 'Kamarul Danial')
insertSort(root, 'Dania Izzah')
insertSort(root, 'Fariz Yazid')
insertSort(root, 'Zharif Aiman')
insertSort(root, 'Sharifa Harun')
insertSort(root, 'Fuad Najma')
insertSort(root, 'Muhd Fakhrul')

printPreorder(root)
print()
printInorder(root)
print()
printPostorder(root)
print()
root.deepestBranch()

