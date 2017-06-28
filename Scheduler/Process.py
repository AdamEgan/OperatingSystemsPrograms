class Process(object):
    #Class for Each Process giving it a time to finish a state which can be
    #Blocked Ready or suspended,A variable for whether it needs input,and
    #An Id to identify it
    def __init__(self,time,state,IO,i_d):
        self.time=time
        self.state=state
        self.IO=IO
        self.i_d=i_d
        self.prioritys=time
        self.currentQueue=0

    def setCurrentQueue(self,que):
        self.currentQueue=que
    def getCurrentQueue(self):
        return self.currentQueue
    def getPriority(self):
        return self.prioritys
    def setPriority(self,pri):
        self.prioritys=pri
    def getTime(self):
        return self.time
    def setTime(self,newtime):
        self.time=newtime
    def getState(self):
        return self.state
    def setState(self,newstate):
        self.state=newstate
    def getId(self):
        return self.i_d
    priority=property(getPriority,setPriority)
    queue=property(getCurrentQueue,setCurrentQueue)
    def __str__(self):
        return ("Id=%s time=%i state=%s"%(self.i_d,self.time,self.state))


    
        
