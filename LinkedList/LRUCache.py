# https://neetcode.io/problems/lru-cache

class DoublyLinkedList:

    def __init__(self,key=None,val=None):
            self.val=val
            self.key=key
            self.next=None
            self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=DoublyLinkedList()
        self.tail=DoublyLinkedList()
        self.head.next=self.tail
        self.tail.prev=self.head

    def addNode(self,node: DoublyLinkedList):
        """Add a new node right after the head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        print(self.head.next.val)

    def removeNode(self,node: DoublyLinkedList):
        """Remove an existing node from the linked list."""
        prev=node.prev
        new=node.next
        prev.next=new
        new.prev=prev
        # print(self.head.next.val)

    def popTail(self):
        """Pop the current tail."""
        res=self.tail.prev
        self.removeNode(res)
        print(res.val)
        return res
        

    def moveToHead(self, node: DoublyLinkedList):
        """Move certain node to the head."""
        self.removeNode(node)
        self.addNode(node)


    def get(self, key: int) -> int:
        if key in self.cache:
            res=self.cache[key]
            self.moveToHead(res)
            return res.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            Newnode=DoublyLinkedList(key,value)
            self.cache[key]=Newnode
            self.addNode(Newnode)

            if len(self.cache)>self.capacity:
                tail=self.popTail()
                # self.cache.pop(tail.key)
                del self.cache[tail.key]
        else:
            node=self.cache[key]
            node.val = value
            self.cache[key]=node
            self.moveToHead(node)
