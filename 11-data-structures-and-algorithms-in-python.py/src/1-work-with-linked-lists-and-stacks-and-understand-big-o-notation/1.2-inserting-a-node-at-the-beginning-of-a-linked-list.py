class Node:
  def __init__(self, data):
    self.value = data
    # Leave the node initially without a next value
    self.next = None

class LinkedList:
  def __init__(self):
    # Set the head and the tail with null values
    self.head = None
    self.tail = None

  def insert_at_beginning(self, data):
    # Create the new node
    new_node = Node(data)
    # Check whether the linked list has a head node
    if self.head:
      # Point the next node of the new node to the head
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node      
      self.head = new_node