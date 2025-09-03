# Question: https://neetcode.io/problems/dynamicArray
class DynamicArray:
    
    def __init__(self, capacity: int):
        if(capacity<= 0):
            print('Please enter a positive value for capacity.')
        self.capacity = capacity
        self.used = 0
        self.items = [None]*capacity
        self.top = -1

    def get(self, i: int) -> int:
    	return self.items[i]

    def set(self, i: int, n: int) -> None:
        if(self.items[i] == None):
            self.used += 1
        self.top = max(self.top, i)
        self.items[i] = n


    def pushback(self, n: int) -> None:
        # self.capacity += 1
        # self.used += 1
        if(self.top+1 == self.capacity):
            self.resize()
        self.used += 1
        self.items[self.top+1] = n
        self.top += 1

    def popback(self) -> int:
        # self.capacity -= 1
        self.used -= 1
        res = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return res

    def resize(self) -> None:
        self.capacity *= 2
        self.items.extend([None]*self.capacity)

    def getSize(self) -> int:
        return(self.used)
    
    def getCapacity(self) -> int:
        return(self.capacity)# - self.used)

dynamicArray = DynamicArray(2)
print([dynamicArray.pushback(1), dynamicArray.pushback(2), dynamicArray.pushback(3), dynamicArray.getSize(), dynamicArray.getCapacity(), dynamicArray.popback(), dynamicArray.getSize(), dynamicArray.getCapacity()])