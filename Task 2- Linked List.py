#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Task 2 - Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

#Add a node to the start of the list
    def addToStart(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

#Display The Linked List
    def displayList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

#Count the total element in the Linked List
    def count(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

#Count the element with Odd number
    def countOdd(self):
        count = 0
        current_node = self.head
        while current_node:
            if current_node.data % 2 != 0:
                count += 1
            current_node = current_node.next
        return count

#Count the element with Even number
    def countEven(self):
        count = 0
        current_node = self.head
        while current_node:
            if current_node.data % 2 == 0:
                count += 1
            current_node = current_node.next
        return count

#Swap between index 1 and 2 of element
    def swap(self, index1, index2):
        if index1 == index2:
            return

        if not self.head or index1 >= self.count() or index2 >= self.count():
            print("Index out of range.")
            return

        if index1 < index2:
            index1, index2 = index2, index1

        current_node = self.head
        current_index = 0
        while current_node:
            next_node = current_node.next
            if current_index == index1:
                temp_data = current_node.data
                break
            current_node = next_node
            current_index += 1

        current_node = self.head
        current_index = 0
        while current_node:
            next_node = current_node.next
            if current_index == index2:
                current_node.data = temp_data
                break
            current_node = next_node
            current_index += 1

#maximum value in Linked List
    def max(self):
        if not self.head:
            print("The list is empty.")
            return

        max_val = self.head.data
        current_node = self.head.next
        while current_node:
            if current_node.data > max_val:
                max_val = current_node.data
            current_node = current_node.next
        return max_val

#minimum value in Linked List
    def min(self):
        if not self.head:
            print("The list is empty.")
            return

        min_val = self.head.data
        current_node = self.head.next
        while current_node:
            if current_node.data < min_val:
                min_val = current_node.data
            current_node = current_node.next
        return min_val

#find range of element in Linked List
    def range(self):
        if not self.head:
            print("The list is empty.")
            return

        min_val = self.min()
        max_val = self.max()
        return max_val - min_val

#total amount of number in Linked List
    def total(self):
        total = 0
        current_node = self.head
        while current_node:
            total += current_node.data
            current_node = current_node.next
        return total

#average element in Linked List
    def average(self):
        total = self.total()
        count = self.count()
        return total / count
    
list = LL()
list.addToStart(10)
list.addToStart(20)
list.addToStart(45)
list.addToStart(35)
list.addToStart(15)

print("Linked List:")
list.displayList()

print("Count:", list.count())
print("Count of Odd Numbers:", list.countOdd())
print("Count of Even Numbers:", list.countEven())

list.swap(1, 5)
print("Linked List after swapping elements at index 1 and 2:")
list.displayList()
list.swap(2, 3)
print("Linked List after swapping elements at index 1 and 2:")
list.displayList()
list.swap(7, 4)
print("Linked List after swapping elements at index 1 and 2:")
list.displayList()

print("Max Value:", list.max())
print("Min Value:", list.min())
print("Range:", list.range())
print("Total:", list.total())
print("Average:", list.average())
