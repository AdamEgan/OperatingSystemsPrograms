#Adam Egan 115359356
from time import sleep
from random import randint
from Process import Process
from ReadyQueue import Queue
class Scheduler(object):
    def __init__(self):
        self.readyQueue=Queue()
        self.blockedQueue=Queue()
        self.TimeQuantam=8
        self.cpu=None
    def addReadyProcess(self,process):
        #Takes in the current process being delt with
        #Then adds to ReadyQueue
        print("Process Added")
        self.readyQueue.enqueue(process)
    def printreadyQueue(self):
        #Prints Items in ReadyQueue
        return("%s"%(self.readyQueue.__str__()))
    def addBlockedProcess(self,process):
        #Add current Blocked Process to the Blocked Queue
        #Checks if the Blocked Process Has received input
        #If not then it asks for input
        #When it receives input it then changes it state to ready
        #And is added back to ReadyQueue
        self.blockedQueue.enqueue(process)
        if process.IO==False:
            print("Enter Something so i can go on ")
            if input(">"):
                process.IO==True
                process.state='Ready'
                self.readyQueue.enqueue(process) 
    def printBlockedQueue(self):
        #Prints Items in BlockedQueue
        return("%s"%(self.blockedQueue.__str__()))
    def addSuspendedProcess(self):
        #Sets the current process in cpu to suspended and adds to readyQueue
        suspended=self.cpu
        self.readyQueue.enqueue(suspended)
    def preemptProcess(self):
        #If time of current process in cpu equally takes away from the timeSlice
        #The process is terminated if so by making the Cpu =None
        #If the time does not subtract evenly it is added back to the readyQueue
        #With a new updated Time
        print("Cpu ready",self.cpu)
        time=self.cpu.getTime()-self.TimeQuantam
        if time <0:
              print("I was finished",self.cpu)
              self.cpu=None
        else:
            print("this wasnt finished",self.cpu)
            time=self.cpu.getTime()
            time-=self.TimeQuantam
            self.cpu.setTime(time)
            self.addReadyProcess(self.cpu)

    def runProcess(self):
        #Dequeues process onto Cpu
        #Checks if it is a blocked process if so adds it to the blocked Queue
        #Else take its time from it and preempt the process
        self.cpu=self.readyQueue.dequeue()
        print("This is on cpu=",self.cpu)
        process=self.cpu
        time=self.cpu.getTime()
        if self.cpu.getState()=="Blocked":
            self.addBlockedProcess(self.cpu)
        else:
            time-=self.TimeQuantam
            process.setTime(time)
            self.preemptProcess()   
def main():
    pro1=Process(16,"Ready",False,"a")
    pro2=Process(8,"Blocked",False,"b")
    pro3=Process(32,"Blocked",False,"c")
    pro4=Process(8,"Ready",False,"d")
    pro5=Process(8,"Ready",False,"e")
    pro6=Process(14,"Ready",False,"f")
    #Adds all processes to ReadyQueue
    sch=Scheduler()
    sch.addReadyProcess(pro1)
    sch.addReadyProcess(pro2)
    sch.addReadyProcess(pro3)
    sch.addReadyProcess(pro4)
    sch.addReadyProcess(pro5)
    sch.addReadyProcess(pro6)
    #Loop for program with random interrupt included
    while sch.readyQueue.length()!=0:
        num=randint(1,5000)
        if  num<100:
            print("Interrupt")
            #sch.addSuspendedProcess()
            sleep(1)
        sch.runProcess()
    print("All processes Complete")
if __name__=='__main__':
    main()
