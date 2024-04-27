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
