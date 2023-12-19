#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499

#Task 2 - Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

#Add a node to the start of the list
    def addToStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


#Display The Linked List
    def displayList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

#count odd number in linked list
    def countOdd(self):
        count_odd = 0
        current = self.head
        while current:
            if current.data % 2 != 0:
                count_odd += 1
            current = current.next
        return count_odd

#count even number in linked list
    def countEven(self):
        count_even = 0
        current = self.head
        while current:
            if current.data % 2 == 0:
                count_even += 1
            current = current.next
        return count_even

#swapping between index
    def swap(self, index1, index2):
        size = self.count()
         #identify if the index within the list
        if index1 < 0 or index2 < 0 or index1 >= size or index2 >= size:
            print("Error: Invalid index")
            return

        current = self.head
        prev1, prev2 = None, None
        for i in range(index1):
            prev1 = current
            current = current.next

        for i in range(index2):
            prev2 = current
            current = current.next

        if prev1:
            prev1.next = current
        else:
            self.head = current

        if prev2:
            prev2.next = current.next
        else:
            self.head = current.next

        current.next, prev1.next, prev2.next = prev1.next, prev2.next, current.next

    def max(self):
        if not self.head:
            print("Error: List is empty")
            return None

        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def min(self):
        if not self.head:
            print("Error: List is empty")
            return None

        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def range(self):
        min_val = self.min()
        max_val = self.max()
        if min_val is not None and max_val is not None:
            return max_val - min_val
        return None

    def total(self):
        total_val = 0
        current = self.head
        while current:
            total_val += current.data
            current = current.next
        return total_val

    def average(self):
        count = self.count()
        if count > 0:
            return self.total() / count
        return None


# Example usage:
linked_list = LL()
linked_list.addToStart(5)
linked_list.addToStart(3)
linked_list.addToStart(8)
linked_list.addToStart(2)

print("Original Linked List:")
linked_list.displayList()

print("Count:", linked_list.count())
print("Count of Odd Numbers:", linked_list.countOdd())
print("Count of Even Numbers:", linked_list.countEven())

linked_list.swap(1, 2)
print("Linked List after swapping elements at index 1 and 2:")
linked_list.displayList()

print("Max Value:", linked_list.max())
print("Min Value:", linked_list.min())
print("Range:", linked_list.range())
print("Total:", linked_list.total())
print("Average:", linked_list.average())
