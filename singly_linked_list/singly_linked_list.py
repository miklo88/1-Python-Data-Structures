class Node:
    #declaring a node class
    def __init__(self, value=None, next_node=None):
        #the nodes value
        self.value = value
        #and the node next to node
        self.next_node = next_node
    
class LinkedList:
    def __init__(self):
        # stores a node at the beginning of the list [0] = None is the default value
        self.head = None
         #stores a node at the end of the list [-1] = None is the default value
        self.tail = None
    
    # returning all the values in the list
    def __str__(self):
        #the output var will be a string
        output = ''
        #self.head is the current_node in the list
        current_node = self.head
        # looping through the list. if current_node isn't anything, we're printing its value
        while current_node is not None:
            # the current_nodes value
            output += f'{current_node.value}'
            #setting the next node to iterate over so you don't print 0 repeatedly
            current_node = current_node.next_node
        # returning the output of our list
        return output
    
    #adding to the head 
    def add_to_head(self):
        #creating a new_node to add
        new_node = Node(value)
        #checking if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #new_node should point to the current head. so looking at {self.head} 
            new_node.next_node = self.head
            #now redeclare the head as the new_node
            self.head = new_node

    #adding to the caboose
    def add_to_tail(self, value):
        # gotta create a new_node again, looks familiar no?
        new_node = Node(value)
        #checking if the list is empty again
        if self.head is None and self.tail is None:
            #if both head and tail are none point to the new_node
            self.head = new_node
            self.tail = new_node
        else:
            #point the node at the current tail, to the new node
            #declaring the next_node as the new_node
            self.tail.next_node = new_node
            #assigning the new_node as the self.tail
            self.tail = new_node

    #removing the head of the list
    def remove_head(self):
        #if list is empty, dont worry about anything
        if not self.head:
            return None
        #if list has one element in it. declare the head and tail as None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # if we have a list full of elements then game on.
        #declaring the head value
        head_value = self.head.value
        #re-assigning self.head to node next to head.
        self.head  = self.head.next_node
        #sending back the new head value
        return head_value

    # # removing from the tail
    # def remove_tail(self):
    #     if not self.tail:
    #         return None
    #     if self.tail.

    #determining how a node is self.head
    def contains(self, value):
        if self.head is None:
            return False
        
        current_node = self.head
        while current_node is not None:

            if current_node.value == value:
                return True
            
            current_node = current_node.next_node

    # def get_max(self):
    # iterate thru the list looking for the highest value. compare values to one another. then reutrn the highest value after total comparisons.

# linked_list = LinkedList()

# linked_list.add_to_head(0)
# linked_list.add_to_tail(6)
# linked_list.add_to_tail(7)
# linked_list.add_to_tail(8)

# print(linked_list)
