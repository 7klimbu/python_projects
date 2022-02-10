import characterclasses as cc
import moveclasses
import turnbasedbattling

# create teams and players
class player():
    def __init__(self):
        self.team = []


playersA = [player()]
playersB = [player()]


for x in range(0, 2):
    createChar = cc.createCharacter(*cc.listOfChars[0])
    playersA[0].team.append(createChar)


for x in range(0, 2):
    createChar = cc.createCharacter(*cc.listOfChars[0])
    playersB[0].team.append(createChar)


# create battle
battle = turnbasedbattling.battle(playersA, playersB)
battle.setup()
