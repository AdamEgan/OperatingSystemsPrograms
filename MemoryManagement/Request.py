class Request(object):
    def __init__(self,Id,KB):
        self.Id =Id
        self.KB=KB

    def getId(self):
        return self.Id

    def setId(self,Id):
        this.Id=Id
    def getKB(self):
        return self.KB
    def setKB(self,KB):
        self.KB=KB

    def __str__(self):
        return ("Request id=%s Size=%skb"%(self.Id,self.KB))
