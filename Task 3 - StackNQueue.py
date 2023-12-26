#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Task 3 - Stack and Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

#Add an element at the start or front end of the list
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            del new_node


#Remove the first element at the start of the list
    def pop(self):
        if self.head is None:
            print("The list is empty")
            return None
        else:
            tempNode = self.head.data
            self.head = self.head.next
        return tempNode

#Add to the end of the list or it will become first of the list if there no element in the list
    def enqueue(self, data):
        current = self.head
        if current is None:
            self.push(data)
            return
        else:
            new_node = Node(data)
            while current.next:
                current = current.next
            current.next = new_node

        del current

#Remove at the start of the list
    def dequeue(self):
        
        if self.head is None:
            print("The list is empty")
            return None
        else:
            tempNode = self.head.data
            self.head = self.head.next
            return tempNode
        
    def reverse(self):  # Reverse the arrangement of the list to display from last to first by inverting the pointers
        current = self.head
        last = None
        while current:
            next = current.next
            current.next = last
            last = current
            current = next

        self.head = last

# display the content of the list
    def displayList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            if current:
                print("-->", end=" ")
        print()
        del current

# # count the number of elements inside the list
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

#Convert current linked list into an array

def convertToArray(listA):
    array = []
    while listA.count():
        array.append(listA.pop())
    array.reverse()
    return array

#Reverse the arrangement of the list
def reverseList(listA, listB):
    while listA.count():
        listB.push(listA.pop())

# Task 3a
listA = LL()
listA.push('P')
listA.push('Y')
listA.enqueue('T')
listA.enqueue('H')
listA.push('O')
listA.enqueue('N')
listA.displayList()
print(listA.count())

listA.pop()
listA.dequeue()
listA.pop()
listA.displayList()
print(listA.count())

# Task 3b
listA = LL()
listA.push('I')
listA.enqueue('L')
listA.enqueue('O')
listA.enqueue('V')
listA.enqueue('E')
listA.push('C')
listA.push('O')
listA.push('D')
listA.push('I')
listA.push('N') 
listA.push('G')
listA.displayList()

arrayA = convertToArray(listA)
listA.displayList()
print(arrayA)

# Task 3c
listA = LL()
listB = LL()
listA.push('I')
listA.enqueue('A')
listA.enqueue('M')
listA.push('A')
listA.enqueue('M')
listA.enqueue('U')
listA.enqueue('S')
listA.enqueue('L')
listA.enqueue('I')
listA.enqueue('M')
listA.displayList()

reverseList(listA, listB)
listA.displayList()
listB.displayList()
