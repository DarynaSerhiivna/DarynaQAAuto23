

class Price:

    def __init__(self, price) -> None:
        self.price = price

    def to_float(self):
        string_price = self.price.replace("\n",".")\
                                 .replace(",","")\
                                 .replace("$","")
        
        return float(string_price)