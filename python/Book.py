class Book:
    def __init__(self, name, author, price) -> None:
        self.__name = name
        self.__author = author
        self.__price = price
    
    # Constructor overloading is not possible in Python
    # Though we can overload by using *args, then if - else's
    
    # def __init__(self, name, author, price, qtyInStock) -> None:
    #     self.__name = name
    #     self.__author = author
    #     self.__price = price
    #     self.__quan = qtyInStock
        
        
    def getName(self):
        return self.__name
    
    def getAuthor(self):
        return self.__author.getName()
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price
        
    def getQtyInStock(self):
        return self.__quan
    
    def setQtyInStock(self, quantity):
        self.__quan = quantity
        
    def __str__(self) -> str:
        return f"{self.__name} by {self.__author} "
