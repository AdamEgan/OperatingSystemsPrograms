class Queue:
    def __init__(self):
        self._data=[None]*10
        self._size=0
        self._front=0
        self._back=(self._front+self._size)%len(self._data)

    def __str__(self):
        output='<-'
        i=self._front
        self._back=self._back+1
        if self._front <self._back:
            print(self._back)
            while i <self._back:
                output=output+str(self._data[i])+'-'
                i=i+1
        else:
            while i<len(self._data):
                output =output+str(self._data[i])+'-'
                i=i+1
            i=0
            while i<self._back:
                output=output+str(self._data[i])+'-'
                i=i+1
        output=output+'<'
        return output

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        item=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        if 0<self._size<len(self._data)//4:
            self.grow(len(self._data)//2)
        return answer
    def enqueue(self,e):
        if self._size==len(self._data):
            self.grow(2*len(self.data))
        self._back=(self._front+self._size)%len(self._data)
        self._data[self._back]=e
        self._size+=1
    def grow(self,cap):
        old_data=self._data
        self._data=[None]*cap
        oldfront=self._front
        for k in range(self._size):
            self._data[k]=old_data[oldfront]
            oldfront=(1+walk)%len(old_data)
        self._front=0


    
    
def main():
    q1=Queue()
    print(q1)
    q1.enqueue('a')
    print(q1)
    q1.enqueue('b')
    print(q1)
    q1.enqueue('c')
    print(q1)
    q1.enqueue('d')
    print(q1)
    q1.enqueue('e')
    print(q1)
    q1.enqueue('a')
    print(q1)
    
if __name__=='__main__':
    main()


