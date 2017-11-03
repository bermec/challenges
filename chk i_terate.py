import random

people = """joe
jeff jerry
johnson"""
total_people = people.split()

family_groups = people.split('\n')

givers = total_people
receivers = people.split()
tup = ()
in_room = []
i = 0
giver = ''

def receive(giver, family_groups, receivers):
    restart = True
    tup = ()
    receiver = random.choice(receivers)

    while restart:
        restart = False
        for family in family_groups:
            if receiver in family and giver in family:
                receiver = random.choice(receivers)
                #restart = True
                break

        tup = (giver, receiver)
        return tup


restart = True
store = []
while restart:
    restart = False
    for giver in givers:
        tup = receive(giver, family_groups, receivers)
        restart = False
        if tup[0] == tup[1]:
            restart = True
            break
        elif tup in store:
            # tup =
            continue


'''

should_restart = True
while should_restart:
  should_restart = False
  for i in range(10):
    print(i)
    if i == 5:
      should_restart = True
      break
'''