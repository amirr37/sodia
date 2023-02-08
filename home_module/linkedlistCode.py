# llist =linkedlist
# methods :
# print llist--------------------------
# addfirst----------------------------
# addlast----------------------------
# add-------------------------------
# size----------------------------------------
# indexof----------------------------------------
# contains---------------------------------------
# removeFirst
# removeLast
# remove
# to array = list(llist)
# address
from typing import Iterator


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getsize(self):
        return self.size

    def add_first(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.tail = node
        self.head = node
        self.size += 1

    def add_last(self, data):

        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def print(self):
        if self.head is None:
            print("linked list is empty.")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def __iter__(self) -> Iterator:
        if self.head is None:
            print("linked list is empty.")
            return
        data, next_item = self.head.data, self.head.next
        yield data
        while next_item is not None:
            data, next_item = next_item.data, next_item.next
            yield data

    def __str__(self):
        if self.head is None:
            return "linked list is empty."
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        return llstr

    def print_head(self):
        print(self.head.data)

    def print_tail(self):
        print(self.tail.data)
        return self.tail.data

    def size(self):
        return self.size

    def add(self, index, data):
        if index == 0:
            self.add_first(data)
        elif index == self.size - 1:
            self.add_last(data)
        else:
            itr_index = 0
            itr = self.head
            next_of_new = None
            if index == 1:
                next_of_new = self.head.next
            while itr_index < index - 1:
                itr = itr.next
                itr_index += 1
                next_of_new = itr.next
            itr.next = Node(data, next_of_new)

    def index_of(self, data):

        itr = self.head
        index = 0
        contains = False
        while index != self.size:
            if data == itr.data:
                contains = True
                break
            itr = itr.next
            index += 1
        if contains:
            print(index)
        else:
            print("data doesn't exist")

    def contains(self, data):
        itr = self.head
        index = 0
        contains = False
        while index != self.size:
            if data == itr.data:
                contains = True
                break
            itr = itr.next
            index += 1
        if contains:
            print(True)
            return True
        else:
            print(False)
            return False

    def get(self, index):
        itr = 0
        node = self.head
        while itr < index:
            node = node.next
            itr += 1
        return node.data

    def __repr__(self):
        if self.head is None:
            return "linked list is empty."
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        return llstr




#
# l1 = LinkedList()
# l1.add_last(0)
# l1.add_last(1)
# l1.add_last(2)
# l1.add_last(3)
# l1.add_last(4)

# print(l1)
# for data in l1:
#     print(data)
