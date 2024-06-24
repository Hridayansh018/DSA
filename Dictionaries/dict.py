stock_price = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = float(tokens[1])
        stock_price.append([day,price])

print(stock_price)

for element in stock_price:
    if element[0] == "march 9":
        print(element[1])


stock_price = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = float(tokens[1])
        stock_price[day] = price

print(stock_price["march 9"])

def get_hash(key):
    h = 0 
    for char in key:
        h += ord(char)
    print(h% 100) 
    return 
    

get_hash("a")
get_hash("b")
get_hash("march 6")

class Hashtable:
    def __init__(self):
     self.MAX = 100
     self.arr = [None for i in range(self.MAX)]

    def g_hash(self,key):
        h = 0 
        for char in key:
            h += ord(char)
        print(h% self.MAX)
        return h% self.MAX

    def __setitem__(self,key,val):
        h = self.g_hash(key)
        self.arr[h] = val
        print(val)

    def __getitem__(self,key):
        h = self.g_hash(key)
        print(self.arr[h])
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.g_hash(key)
        if self.arr[h] is None:
            self.arr[h] = [(key, val)]
        else:
            found = False
            for idx, element in enumerate(self.arr[h]):
                if len(element) == 2 and element[0] == key:
                    self.arr[h][idx] = (key, val)
                    found = True
                    break
            if not found:
                self.arr[h].append((key, val))

    def __delitem__(self, key):
        h = self.g_hash(key)
        if self.arr[h] is not None:
            for idx, element in enumerate(self.arr[h]):
                if len(element) == 2 and element[0] == key:
                    del self.arr[h][idx]
                    return

h = Hashtable()
h["march 6"] = 130
h["march 7"] = 30
h["march 9"] = 70
h["march 3"] = 95
h["dec 6"] = 98
del h["march 7"]
print(h.arr)