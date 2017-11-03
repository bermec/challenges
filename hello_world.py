
class Baby:


    def __init__(self, name):

        self.name = name

    def greeting(self):
        return 'Hello World my name is ' + self.name

if __name__ == '__main__':

    baby = Baby('William')
    greeting = baby.greeting()
    print(greeting)
