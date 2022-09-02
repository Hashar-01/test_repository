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
        
        
    def PrintList(self):
        if self.head==None:
            print("Empty Linked List")
        else:
            #print(self.head.val)
            currentNode=self.head
            while currentNode is not None:
                print(currentNode.val)
                currentNode=currentNode.next
            
    #incomplete
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
        #if self.iterStart:
            #self.iterStart=False
            #self.currentNode=self.head
        #else:
        if self.head==None:
            raise StopIteration
            return("Empty Linked List")
            
        else:
            #print(self.head.val)
            #currentNode=self.head
            #print(self.currentNode.val)
            if self.currentNode is not None:
                value=self.currentNode.val
                self.currentNode=self.currentNode.next
                return value
                
            else:
                #self.iterStart=True
                raise StopIteration
                    
    def deleteEl(self,value):
        currentNode=self.head
        if currentNode.val==value:
            if currentNode==self.tail:
                self.tail=None
            self.head=currentNode.next
            del(currentNode)
            return True
        else:
            while currentNode.next is not None:
                if currentNode.next.val==value:
                    if currentNode.next==self.tail:
                        self.tail=currentNode
                    currentNode.next=currentNode.next.next
                    return True
                currentNode=currentNode.next
            return False  #when not in list
    #deleting entire Linked List
    def deleteL(self):
        if self.head is None and self.tail is None:
            return False
        else:
            self.head=None
            self.tail=None
            
            
    
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
print("----------------------------------")
#n=int(input("enter a value to delete from Linked List:  "))
#print(LList.deleteEl(n))
#for value in LList:
    #print(value)

llist2=linkedList()
llist2.insert(1,-1)
for value in llist2:
    print(value)
llist2.deleteEl(1)
for value in llist2:
    print(value)

print(llist2.tail)
print("-------------------------------------")
LList.__iter__()
print(next(LList))
print([i for i in LList])
print("--------------------- linked list deletion ----------------")
LList.deleteL()
print([i for i in LList])

print("\n"*3)

