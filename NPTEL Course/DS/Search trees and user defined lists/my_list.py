class Node:

    def __init__(self, initval = None):
        self.value = initval
        self.next = None


    def isempty(self):
        return(self.value == None)

    def append(self, v):
        #if the list is an empty list, then add a value to it to create a singleton list
        if self.isempty():
            self.value = v
        #if not empty, then create a new node, point the next of current node to this new node
        #and set its value as v    
        elif self.next == None:
            new_node = Node(v)
            self.next = new_node
        #Recursively append to rest of list. ie the above condition is only if the list
        #is starting from the first node. If they are already filled, then we need to go
        #forward until we reach a node whose next is pointing to none. 
        else:
            (self.next).append(v)
        return()

    def insert(self, head_v):
        #This is for empty list
        if self.isempty():
            self.value = v_head
            return
        #Create an empty node
        new_node = Node()

        #Assign the node pointed to by self as the next node of the new node
        new_node.next = self.next
        #Assign self to point to the new node
        self.next = new_node
        #Set new node value to the value in self
        new_node.value = self.value
        #Set the value in self, as the value passed when insert is called
        self.value = head_v
        return()

    #Remove the first occurence of v
    def delete(self, v):
        if self.isempty():
            return

        #If the node to delete is the head ie the first node
        #If it is a singleton, then we just make the value as None
        if self.value == v:
            self.value = None
            #If it is not the singleton, then we need to 
            #readjust the pointers, then return
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            #if the value is not value to be deleted, then move ahead
            if self.next != None:
                self.next.delete(v)
                #If want to delete the last node, then check if the value is None
                #If yes, then adjust the next pointer to None
                if self.next.value == None:
                    self.next = None
        return

    def sum(self):
        if self.value == None:
            return(0)
        elif self.next == None:
            return(self.value)
        else:
            return(self.value + self.next.sum())

    #print the list
    def __str__(self):
        selflist = []
        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)

        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))

#Create an empty list
l1 = Node()
print(l1.isempty())
l1.append(50)
print(l1.isempty())
#Create a singleton list with value 10
l2 = Node(10)
print(l2.isempty())
print(l1)

l1.append(10)
l1.append(20)
print(l1)
print(l1.sum())
l1.insert(100)
print(l1)
l1.delete(10)
print(l1)
l1.delete(20)
print(l1)
l1.insert(5000)
print(l1)
print(l1.sum())
l1.delete(5000)
print(l1)
l1.delete(20)
print(l1)




