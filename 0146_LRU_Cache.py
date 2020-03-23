class LRUCache:

    class Node:

        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dict = {}

        self.head = LRUCache.Node(0, 0)
        self.tail = LRUCache.Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.dict[key]
        node = self.__remove(node)

        self.__put_front(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if self.size < self.capacity:
            if key not in self.dict:
                node = LRUCache.Node(key, value)

                self.dict[key] = node
                self.__put_front(node)
            else:
                node = self.dict[key]
                node = self.__remove(node)
                node.val = value

                self.__put_front(node)
        else:
            if key not in self.dict:
                node = self.__remove_back()
                del self.dict[node.key]

                node = LRUCache.Node(key, value)

                self.dict[key] = node
                self.__put_front(node)
            else:
                node = self.dict[key]
                node = self.__remove(node)
                node.val = value

                self.__put_front(node)


    def __remove(self, node: Node) -> Node:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.prev = None
        node.next = None

        self.size -= 1

        return node


    def __put_front(self, node: Node) -> None:
        front = self.head.next

        node.next = front
        node.prev = self.head
        front.prev = node

        self.head.next = node
        self.size += 1


    def __remove_back(self) -> Node:
        back = self.tail.prev
        return self.__remove(back)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
