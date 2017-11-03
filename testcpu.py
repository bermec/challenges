import random
rank = ['a', 'b', 'c']
suits = ['a', 'b']
dealt = [('c', 'a')]
num = 0

while num < 2:
    player_rank = random.choice(rank)
    player_suit = random.choice(suits)
    player = (player_rank, player_suit)

    if player not in dealt:
        print(player)
        num += 1
    else:
        continue
    dealt.append(player)