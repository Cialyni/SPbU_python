class Node:
    def __init__(self, object=None):
        self.object = object
        self.next = None


class Mylist:
    def __init__(self):
        self.head = None

    def insert_to_start(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        else:
            new.next = self.head
            self.head = new

    def insert_to_index(self, object, index):
        new = Node(object)
        current = self.head
        position = 0
        if position == index:
            self.insert_to_start(object)
        else:
            while current is not None and position + 1 != index:
                position = position + 1
                current = current.next

            if current is not None:
                new.next = current.next
                current.next = new
            else:
                print("Index Error")

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def delete_at_index(self, index):
        if self.head is None:
            return

        current = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current is not None and position + 1 != index:
                position = position + 1
                current = current.next

            if current is not None:
                current.next = current.next.next
            else:
                print("Index Error")

    def mylist_print(self):
        current = self.head
        while current:
            print(current.object)
            current = current.next
