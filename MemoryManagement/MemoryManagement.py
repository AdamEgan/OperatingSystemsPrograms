from slinkedlist import *
from ReadyQueue import Queue
from Request import Request
class MemoryManagement(object):
    def __init__(self):
        self.mem=SLinkedList()
        self.requests=Queue()
        self.memory=100    #max size of memory
        self.requestsize=0 #size of all requests
        self.request=None  #current request being allocated
    #Makes 4 lists in the linked list representing 4 blocks
    def makeMemory(self):
        for i in range(4):
            self.mem.add_last([])
        return self.mem
    #Main method which allocates first request to be put in a certain block
    #according to its size,this function checks if the memory is full or not
    #if so it deletes the first element in each block as they are the oldest
    def memsize(self):
        requestde=self.requests.dequeue()
        request=requestde.getKB()
        if self.requestsize<self.memory:
            if request >= 0 and request <4:
                self.requestsize+=request
                self.mem.search(0,request)
                print("Added to memory",request)
            elif request >=4 and request <=8:
                self.requestsize+=request
                self.mem.search(1,request)
                print("Added to memory",request)
            elif request>=8 and request <=16:
                self.requestsize+=request
                self.mem.search(2,request)
                print("Added to memory",request)
            elif request >=16 and request <=32:
                self.requestsize+=request
                self.mem.search(3,request)
                print("Added to memory",request)
        else:
            print("request suspended",request)
            self.deleteMem()
    #Deletes first element in each list
    def deleteMem(self):
        self.mem.remove()
    #Prints out structure of the memory       
    def printMemory(self):
        return self.mem.__str__()
    #Adds a request to the queue
    def addMemRequest(self,x):
        print("Request added ",x)
        self.requests.enqueue(x)
    #Prints requests in queue
    def printRequests(self):
        return self.requests.__str__()
def main():
    memory=MemoryManagement()
    memory.makeMemory()
   
    r1=Request(1,2)
    r2=Request(2,10)
    r3=Request(3,30)
    r4=Request(4,32)
    r5=Request(5,31)
    r6=Request(6,29)
    r6=Request(6,2)
    #Add Requests
    memory.addMemRequest(r1)
    memory.addMemRequest(r2)
    memory.addMemRequest(r3)
    memory.addMemRequest(r4)
    memory.addMemRequest(r5)
    memory.addMemRequest(r6)
    print(memory.printRequests())
    print(memory.printMemory())
    #Main loop allocates and deallocates memory 
    while memory.requests.length()!=0:
        memory.memsize()
        print(memory.printMemory())
    print(memory.printMemory())

if __name__=='__main__':
    main()
