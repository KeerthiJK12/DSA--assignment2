class StockSpanner:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def next(self,price):
        span = 1
        if self.s1:
            while self.s1.pop() <= price:
                self.s2.append(self.s1.pop())
                span += 1
        return span    


stock = StockSpanner()
self.s1.append(7)
self.s1.append(1)
self.s1.append(2)
self.s1.append(1)
print(stock.next(2))
