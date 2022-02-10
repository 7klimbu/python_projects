import datetime
import random

gender = {"male":"♂",
               "female": "♀",
               "n/a": "❔"}

listOfChars = []


def indexCharacter(index):
    for char in listOfChars:
        if char[0] == index:
            return char

    raise IndexError("ERROR: INVALID CHARACTER INDEX FOR LISTOFCHARACTERS VARIABLE")


class createCharacter():
    def __init__(self, index, title, rarity, url, gender, bannerColor, footer, startingMoves, stats, ability, elements, series):
        # card desc
        self.index = index
        self.title = title
        self.footer = footer
        self.rarity = rarity
        self.url = url
        self.gender = gender
        self.bannerColor = bannerColor
        self.series = series
        self.elements = elements
        self.owner = "Undefined"

        time = datetime.datetime.now()
        time = time.strftime("%x") +  " (" + time.strftime("%X") + ")"
        self.joinDate = time
        self.haremIndex = 1
        self.teamIndex = 0

        # game stats
        self.level = 1
        self.exp = 0
        self.maxExp = 10
        
        self.HP = random.randint(stats["HP"][0], stats["HP"][1])
        self.MANA = random.randint(stats["MANA"][0], stats["MANA"][1])
        
        self.ATK = random.randint(stats["ATK"][0], stats["ATK"][1])
        self.DEF = random.randint(stats["DEF"][0], stats["DEF"][1])
        self.MAGIC = random.randint(stats["MAGIC"][0], stats["MAGIC"][1])
        self.SPD = random.randint(stats["SPD"][0], stats["SPD"][1])
        self.INT = random.randint(stats["INT"][0], stats["INT"][1])
        self.LCK = random.randint(stats["LCK"][0], stats["LCK"][1])

        # setup battle
        self.battleClone = None
        self.real = None
        self.team = None

        # in-game modifiers
        self.knocked = False
        self.pressTurn = 0
        self.smirk = False
        self.defending = False
        self.abilityActive = True
        self.status = ""
        self.statusEffect = []
        
        self.ATKx = 1
        self.DEFx = 1
        self.MAGICx = 1
        self.SPDx = 1
        self.INTx = 1
        self.LCKx = 1

        # moves
        self.moves = startingMoves
        self.ability = ability

        # items
        self.heldItem = "None"


# kaguya sama
series = "(Kaguya-Sama: Love is War)"
# kaguya s.
startingMoves = ["wack", "freeze"]
startingStats = {
    "HP": [50, 100], "MANA": [50, 100],
    "ATK": [1, 10], "DEF": [1, 10], "MAGIC": [10, 15], "SPD": [1, 10], "INT": [1, 10], "LCK": [1, 10]
}

ability = ["Kokuhaku", "Causes the user to increase their INT stat when faced against the opposite gender."]
elements = ["ice"]
info = ['001', 'Kaguya Shinomiya', "⭐⭐⭐⭐⭐", 'https://cdn.myanimelist.net/images/characters/8/421600.jpg', gender["female"], "red", 'Status: Ready.', startingMoves, startingStats, ability, elements, series]
listOfChars.append(info)

# select and summon a random char
pickRandomChar = random.choice(listOfChars)
createChar = createCharacter(*pickRandomChar)

print(createChar.joinDate)
