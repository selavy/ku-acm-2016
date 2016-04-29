#!/usr/bin/env python

import sys

def convert(card):
    if card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        return int(card)

def unconvert(card):
    if card == 10:
        return 'T'
    elif card == 11:
        return 'J'
    elif card == 12:
        return 'Q'
    elif card == 13:
        return 'K'
    elif card == 14:
        return 'A'
    else:
        return str(card)

if __name__ == '__main__':
    player1 = [convert(x) for x in sys.stdin.readline().rstrip().split()]
    player2 = [convert(x) for x in sys.stdin.readline().rstrip().split()]

    while 1:
        # print "PLAYER 1: ", [unconvert(x) for x in player1]
        # print "PLAYER 2: ", [unconvert(x) for x in player2]
        
        if not player1:
            print "PLAYER 2"
            sys.exit(0)
        elif not player2:
            print "PLAYER 1"
            sys.exit(0)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 > card2:
            player1.extend([card1, card2])
        elif card2 > card1:
            player2.extend([card2, card1])
        else:
            war_chest = []
            while 1:
                if len(player1) < 4:
                    print "PLAYER 2"
                    sys.exit(0)
                elif len(player2) < 4:
                    print "PLAYER 1"
                    sys.exit(0)
                war_chest.append(player1.pop(0))
                war_chest.append(player1.pop(0))
                war_chest.append(player1.pop(0))
                war_chest.append(player2.pop(0))
                war_chest.append(player2.pop(0))
                war_chest.append(player2.pop(0))
                war_chest.append(card1)
                war_chest.append(card2)

                card1 = player1.pop(0)
                card2 = player2.pop(0)
                if card1 > card2:
                    player1.extend([card1, card2])
                    player1.extend(war_chest)
                    break
                elif card2 > card1:
                    player2.extend([card2, card1])
                    player2.extend(war_chest)
                    break
                else:
                    war_chest.append(card1)
                    war_chest.append(card2)

        
