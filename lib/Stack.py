class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        
        if len(self.items) < self.limit:
            self.items.append(item) 
        return self.items
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit
        
    def search(self, target):
        for num in sorted(self.items , reverse=True):
            if num == target:
                return sorted(self.items , reverse=True).index(num)
        return -1
