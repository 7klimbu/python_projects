import copy
import moveclasses
import time

running_battle = []

class side():
    def __init__(self, players):
        uniquePlayers = tuple(players)
        self.characters = []
        
        if len(uniquePlayers) == 1:
            team = players.team
            self.addCharacter(team[0])
            self.addCharacter(team[1])

        if len(uniquePlayers) > 1:
            for p in players:
                startingChar = p.team[0]
                self.addCharacter(startingChar)


    def addCharacter(self, character):
        if character.knocked == False:
            if character.battleClone == None:
                character.battleClone = copy.deepcopy(character)
                character.battleClone.real = character
 
            self.characters.append(character.battleClone)
            character.team = self
            
            return True
        else:
            return False


    def replaceCharacter(self, oldCharacter, newCharacter):
        if newCharacter.knocked == False:
            if newCharacter.battleClone == None:
                newCharacter.battleClone = copy.deepcopy(character)
                character.battleClone.real = character

            replaceItem(self.characters, oldCharacter, newCharacter)
            character.team = self
            
            return True
        else:
            return False

    

def replaceItem(table, oldItem, newItem):
    i = table.index(oldItem)
    table.insert(item, i)
    table.remove(oldItem)


# if there is one player on a side, he controls both characters
# if there are two, control over each character is split up
# if there is three, the same also applies
def returnControllers(players):
    if len(players) == 1:
        return [players[0], players[0]]

    if len(players) == 2:
        return [players[0], players[1]]

    if len(players) == 3:
        return [players[0], players[1], players[2]]


class battle():
    def __init__(self, sideAPlayers, sideBPlayers):
        self.turn = 0
        self.running = True
        self.commandList = []
        self.sideAPlayers = returnControllers(sideAPlayers)
        self.sideBPlayers = returnControllers(sideBPlayers)
        self.sides = {}


    def setup(self):
        # create sides
        createSideA = side(self.sideAPlayers)
        self.sides["A"] = createSideA

        createSideB = side(self.sideBPlayers)
        self.sides["B"] = createSideB

        # start battle
        self.continueTurn()


    # game loop
    def continueTurn(self):
        time.sleep(1)
        
        self.commandList = []
        sides = self.sides
        self.turn += 1
        print("turn", self.turn)

        def getCommand(character, userTeam, enemyTeam):
            if character != None:
                playerid = character.owner
                return self.chooseCommand(playerid, character, userTeam, enemyTeam)


        # choosing attacks
        for character in sides["A"].characters:
            userTeam = sides["A"]
            enemyTeam = sides["B"]
            
            cmd = getCommand(character, userTeam, enemyTeam)
            self.commandList.append(cmd)
                
        for character in sides["B"].characters:
            userTeam = sides["B"]
            enemyTeam = sides["A"]
            
            cmd = getCommand(character, userTeam, enemyTeam)
            self.commandList.append(cmd)

        self.playTurn()


    def chooseCommand(self, playerid, user, userTeam, enemyTeam):
        move = moveclasses.moveList["wack"]
        move.user = user
        move.targets = [enemyTeam.characters[0]]
        
        return move


    def playTurn(self):
        def sideCanBattle(sidePlayers):
            playersWithNoTeam = 0

            # check which players still have characters that can fight
            for player in sidePlayers:
                for character in player.team:
                    if character.knocked == False:
                        break

                    if character == player.team[len(player.team) - 1]:
                        playersWithNoTeam += 1


            if playersWithNoTeam == len(sidePlayers):
                return False
            else:
                return True
            

        # execute all moves which have been listed (spd not taken into account yet)
        for move in self.commandList:
            move.execute(move, move.user, move.targets, move.user.team, self.sides["A"])

            sideADefeated = not sideCanBattle(self.sideAPlayers)
            sideBDefeated = not sideCanBattle(self.sideBPlayers)

            if sideADefeated or sideBDefeated:
                self.running = False
                break


        # if game is not over, loop
        if self.running:
            self.continueTurn()
                
                
