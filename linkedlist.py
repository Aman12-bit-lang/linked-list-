class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new

    def print_list(self):
        cur = self.head
        if not cur:
            print("List is empty.")
            return
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("List is empty.")
        if n == 1:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(n - 2):
            if not cur.next:
                raise IndexError("Index out of range.")
            cur = cur.next
        if not cur.next:
            raise IndexError("Index out of range.")
        cur.next = cur.next.next

# Sample test
ll = LinkedList()
ll.add_to_end(10)
ll.add_to_end(20)
ll.add_to_end(30)
ll.print_list()
try:
    ll.delete_nth_node(2)
except IndexError as e:
    print("Error:", e)
ll.print_list()
