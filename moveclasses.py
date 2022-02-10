import math
import random
import type_matchups
math.clamp = lambda value, lower, upper: lower if value < lower else upper if value > upper else value

# stat formulas
powerMultiplier = lambda power: 3 + (power * 0.00267)
calculateDamage = lambda power, attackerATK, enemyDEF: math.sqrt(attackerATK)** power/(enemyDEF)
calculateAccuracy = lambda attackerSPD, enemySPD: (1/((1 + enemySPD/attackerSPD) * 0.7)) * 100

# funcs to decide whether move uses accuracy
def moveUsesAccuracy(func):
    def wrapper(move, user, targets, userTeam, targetTeam):
        for target in targets:
            # which stats the move uses to affect hit chances
            hitAttr = move.statPurpose["Hit Chance"]
            missAttr = move.statPurpose["Miss Chance"]
            
            # lowest % to hit is 1%, highest is 99%
            accuracy = calculateAccuracy(getattr(user, hitAttr), getattr(target, missAttr))
            accuracy = math.clamp(accuracy, 1, 99)

            # roll chance to hit
            rng = random.randint(1, 100)

            if accuracy > rng:
                func(move, user, target, userTeam, targetTeam)
                print(move.name, " landed!")
            else:
                print(move.name, " missed!")


    return wrapper


def moveAlwaysHits(move):
    def wrapper(move, user, targets, userTeam, targetTeam):
        for target in targets:
            move(move, user, target, userTeam, targetTeam)

    return wrapper


# applying elemental weaknesses/strengths
def elementalMultiplier(move, target):
    elements = type_matchups.elements
    
    multiplier = 1

    for element in target.elements:
        if move.element in elements[element]["Weak"]:
            multiplier *= 2

        if move.element in elements[element]["Strong"]:
            multiplier *= 0.5

        if move.element in elements[element]["Null"]:
            multiplier = 0
        

    return multiplier


# standard moves
@moveUsesAccuracy
def deployAttack(move, user, target, userTeam, targetTeam):
    atkAttr = move.statPurpose["Move Offense"]
    defAttr = move.statPurpose["Target Defense"]

    power = powerMultiplier(move.power)
    damage = calculateDamage(power, getattr(user, atkAttr), getattr(target, defAttr))

    # apply elemental effect
    multiplier = elementalMultiplier(move, target)
    damage *= multiplier
    target.HP -= damage

    if target.HP <= 0:
        print(target.title, "died")
        target.real.knocked = True


# custom moves
# w.i.p


# move class
class move():
    def __init__(self, name, power, element, manaCost, statPurpose, moveFunction):
        self.name = name
        self.power = power
        self.element = element
        self.statPurpose = statPurpose
        self.manaCost = manaCost
        self.execute = moveFunction

        self.user = "Unspecified"
        self.targets = []


# move list
moveList = {}

# wack
statPurpose = {"Move Offense": "ATK" , "Target Defense": "DEF" , "Hit Chance": "SPD" , "Miss Chance": "SPD"}
name = "wack"
moveList[name] = move(name, 20, "Normal", 0, statPurpose, deployAttack)

# freeze
statPurpose = {"Move Offense": "ATK" , "Target Defense": "DEF" , "Hit Chance": "SPD" , "Miss Chance": "SPD"}
name = "freeze"
moveList[name] = move(name, 30, "Ice", 10, statPurpose, deployAttack)
