class DoublyLinkedList : 
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.size = 0
            self.dummyHead = self.Node(None)
            self.dummyTail = self.Node(None)
            self.dummyHead.next=self.dummyTail
            self.dummyTail.prev=self.dummyHead
            
    def __str__(self):
        s = ''
        p = self.dummyHead.next
        for i in range(self.__len__()) :
            s += str(p.data) + ' '
            p = p.next
        return s

    def print(self):
        s = ''
        p = self.dummyHead.next
        for i in range(self.__len__()) :
            s += str(p.data) + " -> " if p.next is not self.dummyTail else str(p.data)
            p = p.next
        return s

    def __len__(self) :
        return self.size
        
    def isEmpty(self) :
        return self.size == 0
    
    def insertBefore(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1
        
    def append(self,data) :
        newNode = self.Node(data)
        if self.size == 0 :
            self.dummyHead.next = newNode
            self.dummyTail.prev = newNode
            newNode.prev = self.dummyHead
            newNode.next = self.dummyTail
            
        else :
            self.dummyTail.prev.next = newNode
            newNode.prev = self.dummyTail.prev
            self.dummyTail.prev = newNode
            newNode.next=self.dummyTail
        self.size += 1   

    def setHead(self,i):                                
        x = self.Node(i)
        x.next = self.dummyHead.next
        self.dummyHead.next.prev=x
        self.dummyHead.next = x
        x.prev = self.dummyHead
        self.size+=1

    def dataOf(self,i):
        q = self.dummyHead.next
        for j in range(len(self)) :
            if j == i :
                return q.data
            q = q.next
        return -1

    def insert(self,data):
        q = self.dummyHead.next
        if self.isEmpty():
            self.append(data)
        elif self.__len__()==1:
            if q.data > data:
                self.append(data)
            else:
                self.setHead(data)
        else:
            for i in range(self.__len__()):
                if q.data < data:
                    self.insertBefore(q,data)
                    break
                elif q.next == self.dummyTail:
                    self.append(data)
                    break
                else:
                    q=q.next
        
    def clear(self):
        self.size = 0
        self.dummyHead = self.Node(None)
        self.dummyTail = self.Node(None)
        self.dummyHead.next=self.dummyTail
        self.dummyTail.prev=self.dummyHead                
        
def getMaxBits(n):
    i=0
    while n>0:
        n//=10
        i += 1
    return i

def sort(x,i):
    y=x
    x=abs(x)
    for j in range(i):
        x//=10
    if x%10==0:
        l0.insert(y)
    elif x%10==1:
        l1.insert(y)
    elif x%10==2:
        l2.insert(y)
    elif x%10==3:
        l3.insert(y)
    elif x%10==4:
        l4.insert(y)
    elif x%10==5:
        l5.insert(y)
    elif x%10==6:
        l6.insert(y)
    elif x%10==7:
        l7.insert(y)
    elif x%10==8:
        l8.insert(y)
    elif x%10==9:
        l9.insert(y)

def nextRound():
    tl.clear()
    for i in range(l0.__len__()):
        tl.append(l0.dataOf(i))
    for i in range(l1.__len__()):
        tl.append(l1.dataOf(i))
    for i in range(l2.__len__()):
        tl.append(l2.dataOf(i))
    for i in range(l3.__len__()):
        tl.append(l3.dataOf(i))
    for i in range(l4.__len__()):
        tl.append(l4.dataOf(i))
    for i in range(l5.__len__()):
        tl.append(l5.dataOf(i))
    for i in range(l6.__len__()):
        tl.append(l6.dataOf(i))
    for i in range(l7.__len__()):
        tl.append(l7.dataOf(i))
    for i in range(l8.__len__()):
        tl.append(l8.dataOf(i))
    for i in range(l9.__len__()):
        tl.append(l9.dataOf(i))

    l0.clear()
    l1.clear()
    l2.clear()
    l3.clear()
    l4.clear()
    l5.clear()
    l6.clear()
    l7.clear()
    l8.clear()
    l9.clear()

def check():
    c=0
    if l1.isEmpty():
        c+=1
    if l2.isEmpty():
        c+=1
    if l3.isEmpty():
        c+=1
    if l4.isEmpty():
        c+=1
    if l5.isEmpty():
        c+=1
    if l6.isEmpty():
        c+=1
    if l7.isEmpty():
        c+=1
    if l8.isEmpty():
        c+=1
    if l9.isEmpty():
        c+=1
    return c

def merge():
    if l1.isEmpty()==False:
        for i in range(l1.__len__()):
            l0.insert(l1.dataOf(i))
    elif not l2.isEmpty:
        for i in range(l2.__len__()):
            l0.insert(l2.dataOf(i))
    elif not l3.isEmpty:
        for i in range(l3.__len__()):
            l0.insert(l3.dataOf(i))
    elif not l4.isEmpty:
        for i in range(l4.__len__()):
            l0.insert(l4.dataOf(i))
    elif not l5.isEmpty:
        for i in range(l5.__len__()):
            l0.insert(l5.dataOf(i))
    elif not l6.isEmpty:
        for i in range(l6.__len__()):
            l0.insert(l6.dataOf(i))
    elif not l7.isEmpty:
        for i in range(l7.__len__()):
            l0.insert(l7.dataOf(i))
    elif not l8.isEmpty:
        for i in range(l8.__len__()):
            l0.insert(l8.dataOf(i))
    elif not l9.isEmpty:
        for i in range(l9.__len__()):
            l0.insert(l9.dataOf(i))

tl=DoublyLinkedList()
og=DoublyLinkedList()
l0=DoublyLinkedList()
l1=DoublyLinkedList()
l2=DoublyLinkedList()
l3=DoublyLinkedList()
l4=DoublyLinkedList()
l5=DoublyLinkedList()
l6=DoublyLinkedList()
l7=DoublyLinkedList()
l8=DoublyLinkedList()
l9=DoublyLinkedList()

y = input("Enter Input : ").split()
y = list(map(int, y))
x=y.copy()
x =  [abs(ele) for ele in x]
x.sort()
num=0
for i in range(len(y)):
    tl.append(y[i])
    og.append(y[i])
if len(x)>1:
    for i in range(getMaxBits(x[-2])+1):
        for j in range(tl.__len__()):
            sort(tl.dataOf(j),i)   
        print("------------------------------------------------------------")
        print("Round :",i+1)
        print("0 :",l0)
        print("1 :",l1)
        print("2 :",l2)
        print("3 :",l3)
        print("4 :",l4)
        print("5 :",l5)
        print("6 :",l6)
        print("7 :",l7)
        print("8 :",l8)
        print("9 :",l9)
        if check()>8:
            merge()
            num = i
            break
        if i <getMaxBits(x[-2]):
            nextRound()
        num+=1  
    print("------------------------------------------------------------")
    print(num,"Time(s)")
    print("Before Radix Sort :",og.print())
    print("After  Radix Sort :",l0.print())
else:
    print("------------------------------------------------------------")
    print("0 Time(s)")
    print("Before Radix Sort :",og.print())
    print("After  Radix Sort :",og.print())