class Queue:
    """ Reasonably efficient implementation of the Queue ADT.

        Efficient dequeuing, and efficient space use when enqueuing
		Could be improved by:
		1. modular arithmetic to simplify the code for wrapping around the list
		2. a 'shrink' policy to reduce underlying list when too much unused space
    """
    def __init__(self):
        self.body = [None] * 10
        self.head = 0    #index of first element, unless empty, and then 0 by default
        self.tail = 0    #index of free cell for next element
        self.size = 0    #number of elements in the queue

    def __str__(self):
        output = '<-'
        i = self.head
        if self.head < self.tail:
            while i < self.tail:
                output = output + str(self.body[i]) + '-'
                i = i+1
        else:
            while i < len(self.body):
                output = output + str(self.body[i]) + '-'
                i = i+1
            i = 0
            while i < self.tail:
                output = output + str(self.body[i]) + '-'
                i = i+1
        output = output + '<'
        return output
    def grow(self):
        oldbody = self.body
        self.body = [None] * (2*self.size)
        oldpos = self.head
        pos = 0
        if self.head < self.tail:     #data is not wrapped around in list
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None           
                pos = pos + 1
                oldpos = oldpos + 1
        else:                         #data is wrapped around
            while oldpos < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None           
                pos = pos + 1
                oldpos = oldpos + 1
            oldpos = 0
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        self.head = 0
        self.tail = self.size 
         

    def enqueue(self,item):
        if self.size == 0:
            self.body[0] = item      #assumes an empty queue has head at 0
            self.size = 1
            self.tail = 1
        else:
            self.body[self.tail] = item
            self.size = self.size + 1
            if self.size == len(self.body):  #list is now full
                self.grow()                  #so grow it ready for next enqueue
            elif self.tail == len(self.body)-1:  #no room at end, but must be at front
                self.tail = 0
            else:
                self.tail = self.tail + 1

    def dequeue(self):
        if self.size == 0:     #empty queue
            return None
        item = self.body[self.head]
        self.body[self.head] = None
        if self.size == 1:                #just removed last element, so rebalance
            self.head = 0
            self.tail = 0
            self.size = 0
        elif self.head == len(self.body) - 1:  #if the head was the end of the list
            self.head = 0                 #we must have wrapped round, so point to start
            self.size = self.size - 1
        else:            
            self.head = self.head + 1          #just move the pointer on one cell
            self.size = self.size - 1
        #we haven't changed the tail, so nothing to do
        return item

    def length(self):
         return self.size




