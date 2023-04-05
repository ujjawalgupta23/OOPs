class Author:
    # __name = "ujjawal"
    
    def __init__(self, name, email, gender) -> None:
        self.__name = name
        self.__email = email
        self.__gender = gender
        
    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getGender(self):
        return self.__gender
    
    def setEmail(self, email):
        self.__email= email
        
    def __str__(self):
        return f'{self.__name} ({self.__gender}) at {self.__email}'
    
def hello():
    print("Hi how are you")


if __name__ == "__main__":
    hello()
