
class test:

    DATA = 7


    def __init__(self, data):
        self.data = data

    def output(self):
        self.DATA += + 2
        return self.DATA

    def output2(self):
        self.data *= 2 + self.DATA
        return self.data

    def local_var(self, num):
        chk = self.data + num
        return chk


if __name__ == '__main__':

    var_test = test(2)
    #print(var_test.output())
    #print(var_test.output2())
    print(var_test.local_var(7))

''' incoming number is data (self.data) order of calling of function will alter its value'''