class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def discount(self,dis):
        off_price = (dis/100)*self.price
        return self.price_of 
l1 = Laptop('hp','xpsjf85',50000)
l2 = Laptop('dell','podhe14',80000)

print(l1.brand_name)
print(l2.brand_name)
print(l2.discount(40))