class Height:
    def __init__(self, tall):
        self.tall = tall
        print('{0} is the number.'.format(self.tall))
class Width:
    def __init__(self, breadth):
        self.breadth = breadth
# --------------------------------------

class Person:
    def sayhi(self):
        print('Hello, how are you?')
        
if __name__ == "__main__":
    Height(0)
    
    b = Width(5)
    
    
    p =Person()
    p.sayhi()
    # or
    Person().sayhi()
    