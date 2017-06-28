from time import sleep
from random import randint
from Process import Process
from ReadyQueue import Queue
class MultiLevel(object):
    def __init__(self):
        self._Queues=[Queue()for i in range(8)]
        self.Cpu=None
        self._time=0
    def printQueue(self):
        print(self._Queues)
    def addProcess(self,process):
        priority = process.getPriority()
        if priority >= 4 and priority < 8:
            self._Queues[0].enqueue(process)
        elif priority >= 8 and priority < 16:
            self._Queues[1].enqueue(process)
        elif priority>= 16 and priority < 32:
            self._Queues[2].enqueue(process)
        elif priority >= 32 and priority < 64:
            self._Queues[3].enqueue(process)
        elif priority>= 64 and priority < 128:
            self._Queues[4].enqueue(process)
        elif  priority>= 128 and priority < 256:
            self._Queues[5].enqueue(process)
        elif priority >= 256 and priority < 512:
            self._Queues[6].enqueue(process)
        elif priority>= 512 :
            self._Queues[7].enqueue(process)
    def printreadyQueue(self):
        for i in range(8):
            if self._Queues[i].length() >0:
                print("Queue%i=%s"%(i,self._Queues[i].__str__()))
    def runProcess(self):
        if self._Queues[0].length() > 0:
            self.cpu = self._Queues[0].dequeue()
            self._time = 4 #2*0+2
            self.cpu.setCurrentQueue(0)
            self.runprocess2(self.cpu)
            
        elif self._Queues[1].length() > 0:
            self.cpu = self._Queues[1].dequeue()
            self._time = 8
            self.cpu.setCurrentQueue(1)
            self.runprocess2(self.cpu)
        elif self._Queues[2].length() > 0:
            self.cpu = self._Queues[2].dequeue()
            self._time = 16
            self.cpu.setCurrentQueue(2)
            self.runprocess2(self.cpu)
        elif self._Queues[3].length() > 0:
            self.cpu = self._Queues[3].dequeue()
            self._time = 32
            self.cpu.setCurrentQueue(3)
            self.runprocess2(self.cpu)
        elif self._Queues[4].length() > 0:
            self.cpu = self._Queues[4].dequeue()
            self._time = 64
            self.cpu.setCurrentQueue(4)
            self.runprocess2(self.cpu)
        elif self._Queues[5].length() > 0:
            self.cpu = self._Queues[5].dequeue()
            self._time = 128
            self.cpu.setCurrentQueue(5)
            self.runprocess2(self.cpu)
        elif self._Queues[6].length() > 0:
            self.cpu = self._Queues[6].dequeue()
            self._time = 256
            self.cpu.setCurrentQueue(6)
            self.runprocess2(self.cpu)
        elif self._Queues[7].length() > 0:
            process = self._Queues[7].dequeue()
            self._time = 512
            self.cpu.setCurrentQueue(7)
            self.runprocess2(self.cpu)

    def runprocess2(self,process):
       print("Run process on",process)
       if self.cpu.getState()=="Blocked":
           print("Im Blocked Increase my Level",self.cpu)
           process.priority=process.priority*2
           process.queue+=1
           print("Enter Something so i can go on ")
           if input(">"):
               process.state='Ready'
               self.addProcess(process)
       else:
           self.preemptProcess()
                

           
    def preemptProcess(self):
        time=self.cpu.getTime()-self._time
        if time <=0:
            print("I was Finished %s,Level=%i"%(self.cpu,self.cpu.getCurrentQueue()))
            self.cpu=None
        else:
            print("this wasnt finished",self.cpu)
            time=self.cpu.getTime()
            time-=self._time
            self.cpu.setTime(time)
            self.cpu.priority=self.cpu.priority*2
            self.cpu.queue+=1
            self.addProcess(self.cpu)
        
        







def main():
    pro1=Process(4,"Ready",False,"a")
    pro2=Process(8,"Blocked",False,"b")
    pro3=Process(32,"Blocked",False,"c")
    pro4=Process(8,"Ready",False,"d")
    pro5=Process(8,"Ready",False,"e")
    pro6=Process(14,"Ready",False,"f")
    sch=MultiLevel()
    sch.addProcess(pro1)
    sch.addProcess(pro2)
    sch.addProcess(pro3)
    sch.addProcess(pro4)
    sch.addProcess(pro5)
    sch.addProcess(pro6)
    sch.printreadyQueue()
    for i in range(8):
        while sch._Queues[i].length()!=0:
            num=randint(1,5000)
            if num <200:
                print("Interrupt")
                sleep(1)
            sch.runProcess()
            sch.printreadyQueue()
    sch.printreadyQueue()



if __name__=='__main__':
    main()
