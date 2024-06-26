class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        dllstr = ''

        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next
        print(dllstr)


    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked List is empty")
            return
    
        last_node = self.get_last_node()
        itr = last_node
        dllstr = ''
      
        while itr:
            dllstr += itr.data + '-->'
            itr = itr.prev
        print("Linked List in reverse: ", dllstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None 
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()