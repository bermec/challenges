'''
It's 2001 all over again, and you just got a brand new ps2 in the mail.
Unfortunately, it only has 2 controller ports, and you have N friends
who all want to play at the same time.

Fortunately, however, the ps2 has an accessory called a 'multitap'
that multiplexes one controller port into four controller ports, to
allow more than 2 controllers at once.

Pretend you don't know that only one multitap can be used in a given
PS2 at once. By connecting multitaps to multitaps, you could easily
create a complicated tree architecture to get as many ports as you need.
However, you also have limited resources at your disposal.

Given that a controller costs $20, and a multitap costs $12, write a
function that takes in an integer D for the amount of money you have
(in dollars) and returns the total maximum number of people you could
afford to get to play with you on one ps2 tree.

For example, the ps2 has 2 ports to start with and comes with 1
controller, so if D < 20, then the function should return 1. However,
when you add another $20, you can afford another controller, so for
D = 20, the function should return 2. Adding another controller costs
you not only another $20 for the controller, but also $12 for the first
multitap to go into the system, so for 20<=D<(40+12), you should return N=3.

This is tricky because once you get >5 controllers, you need ANOTHER
multitap...and greater than 8 controllers you need 3+ multitaps.

'''

def controllers(cash):
    CONTROLLER = 20
    MULTITAP = 12
    # multitap + 3 controllers, 1port used for extra multitap
    multitap_assembly = MULTITAP + CONTROLLER * 3
    total_cash = cash + CONTROLLER  # one controller comes with the ps2
    multitap_assemblies_required = total_cash // multitap_assembly
    remaining_cash = total_cash % multitap_assembly
    extra_controllers = remaining_cash // CONTROLLER
    total_players = multitap_assemblies_required * 3 + extra_controllers
    return total_players


if __name__ == '__main__':

    cash = 1400
    ans = controllers(cash)
    print('Players: ', ans)