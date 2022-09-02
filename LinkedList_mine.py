class node:
    def __init__(self,value=None):
        self.val=value
        self.next=None

class linkedList: 
    def __init__(self):
        self.head=None
        self.tail=None
        self.iterStart=True
        
        
    def insert(self,value,pos=-1):
        newNode=node(value)
        #if it is empty
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        #insertion at start
        elif pos==0:
            newNode.next=self.head
            self.head=newNode
        #insertion at end
        elif pos==-1:
            self.tail.next=newNode
            self.tail=newNode
        else:
            index=1
            currentNode=self.head
            while currentNode is not None and index<pos-1:
                index+=1
                currentNode=currentNode.next
            newNode.next=currentNode.next
            currentNode.next=newNode
        # insert at any position
        
    def EndInsert(self,value):
        
        tempNode= node(value)
        
        if self.head is None:
            self.head=tempNode
            self.tail=tempNode
        else:
            self.tail.next=tempNode
            self.tail=tempNode
        
        
    def PrintList(self):
        if self.head==None:
            print("Empty Linked List")
        else:
            #print(self.head.val)
            currentNode=self.head
            while currentNode is not None:
                print(currentNode.val)
                currentNode=currentNode.next
            
    def sort(self):
        currentNode=self.head
        while currentNode.next is not None:
            if currentNode.val > currentNode.next.val:
                currentNode.val,currentNode.next.val =currentNode.next.val,currentNode.val  #swap the value not the address
            currentNode=currentNode.next
    def min(self):
        currentNode=self.head
        min=self.head.val
        while currentNode is not None:
            if min>currentNode.val:
                min=currentNode.val
            currentNode=currentNode.next
        return min
    
    def __iter__(self):
        self.currentNode=self.head
        return self
        
    def __next__(self):
        if self.iterStart:
            self.iterStart=False
            #self.currentNode=self.head
        else:
            if self.head==None:
                print("Empty Linked List")
            else:
                #print(self.head.val)
                #currentNode=self.head
                #print(self.currentNode.val)
                if self.currentNode is not None:
                    value=self.currentNode.val
                    self.currentNode=self.currentNode.next
                    return value
                    
                else:
                    self.iterStart=True
                    raise StopIteration
LList=linkedList()
#print(LList.head)
for i in range(50,0,-2):
    LList.insert(i,-1)
for i in range(1,10):
    LList.insert(i,10)
LList.sort()
#LList.PrintList()
print("minimum num: ",LList.min())
for value in LList:
    print(value)

