"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

  
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
        
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        
        # check if DLL is empty by seeing if the head and tail are none
        if self.head is None and self.tail is None:
            # if it is, set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
            # increment to DLL length attribute
            self.length += 1

        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node
            # increment 
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Nodepython3 test_doubly_linked_list.py -v.
    """
    def remove_from_head(self):
        # store the value of the head
        value = self.head.value
        # delete the head

            # if next is not None
        if self.head.next is not None:
                # set head.next's prev to None
            self.head.next = None
                # set head value to head.next
            value = self.head.next
            # else (if head.next is None) (we know there is only one item)
        elif self.head.next is None:
                # set head to None
            self.head = None
                # set tail to None
            self.tail = None
              # decrement the length of the DLL
            self.length -= 1

        # return the value
        return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)

        # if DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node
            # increment the DLL length attribute
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        value = self.tail.value
        # decrement the length of the DLL
        # delete the tail
        if self.tail.prev is None:
                # set tail to None
            self.tail = None
                # set head to None
            self.head = None
                # decrement
            self.length -= 1
        else:
            value.prev.next = value.next
            value.next.prev = value.prev
            self.length -= 1
        # return the value
        return value        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        if value is self.head.value:
            pass
        elif value is self.tail.value:
            self.add_to_head(value)
            node = None
            self.length -= 1
        else:
            cur = self.head.value
            while cur.next is not None:
                if cur == node:
                    self.add_to_head(value)
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.length -= 1
                    return
                cur = cur.next



        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        if value is self.tail.value:
            return
        elif value is self.head.value:
            self.add_to_tail(value)
            node = None
            self.head = self.head.next
            self.length -= 1
        else:
            cur = self.tail
            while cur is not None:
                if cur == node:
                    self.add_to_tail(value)
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.length -= 1
                    return
                cur = cur.prev




    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        #decrement
        self.length -= 1

        #if you are deleting the head then you need to reassign the head to the next placeholder
        if self.head is node:
            self.head = node.next

        if self.head is None:
            self.tail = None

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List. you have to reverse the current list and find the maximum
    """
    def get_max(self):
        if self.head is None:
            return
        current = self.head
        max = 0
            #If value of max is lesser than current's data  
            #Then, replace value of max with current node's data  
        while current != None:
            if max < current.value:
                max = current.value
            current = current.next
        return max
        