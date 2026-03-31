class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = 0
        self.array = []



    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.index == self.capacity:
            self.resize()
        self.array.append(n)
        self.index += 1


    def popback(self) -> int:
        self.index -= 1
        value = self.array[self.index]
        
        return value
 

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.index
        
    def getCapacity(self) -> int:
        return self.capacity
