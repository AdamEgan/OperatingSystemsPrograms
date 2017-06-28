""" Classes to implement a singly linked list. """

class SLLNode:
    """ An internal node in a singly linked list. """
    def __init__(self, item, nextnode):
        self._element = item    #any object
        self._next = nextnode
class SLinkedList:
    """ A singly linked list. """
    def __init__(self):
        self._first = None      #an SLLNode
        self._size = 0          #an integer
        self._cursor=None
    def __str__(self):
        """ Return a string representation of the list. """
        outstr = "-"
        node = self._first
        while node:
            outstr = outstr + str(node._element) + "-"
            #can access node's private variable, because defined in this file
            node = node._next
        return outstr
    def getElement(self,index):
        num=0
        self._cursor=self._first
        while num<index:
            self._cursor=self._cursor._next
            num+=1
        return self._cursor._element
    def search(self,x,y):
        num=0
        self._cursor=self._first
        while num <x:
            self._cursor=self._cursor._next
            num+=1
        self._cursor._element+=[y]
    def remove(self):
        self._cursor=self._first
        count=0
        while count!=self.length():
            if len(self._cursor._element)!=0:
                ele=self._cursor._element.pop(0)
            print("removed",ele)
            self._cursor=self._cursor._next
            count+=1
    def add_last(self, element):
        """ Add element to the end of the list. """
        newnode = SLLNode(element, None)
        if self._first == None:
            self._first = newnode
        else:                #iterate through list to find last
            node = self._first
            while node._next:
                node = node._next
            node._next = newnode
        self._size = self._size + 1
    def length(self):
        """ Return the number of elements in the list. """
        return self._size



    

                
                
                
        
        
        
    
    
        

