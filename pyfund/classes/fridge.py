''' Demonstrate raiding a refridgerator '''

from contextlib import closing

class RefridgeratorRaider:
    ''' raid a fridge '''

    def open(self):
        print('Open fridge door.')


    def take(self, food):
        print('Finding {0}... '.format(food))
        if food == 'deep fried pizza':
            raise RuntimeError('Health warning!')
        print('Taking {} '.format(food))

    def close(self):
        print('Close fridge door.')


def raid(food):

    with closing(RefridgeratorRaider()) as r:
        r.open()
        r.take(food)


if __name__ == '__main__':
    raid('deep fried pizza')