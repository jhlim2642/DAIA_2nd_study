import random
import time

class Player:

    def __init__(self, hp, mp, stem):
        self.hp = hp
        self.mp = mp
        self.stem = stem
        self.attackPower = 5
        self.deffencePower = 3
        self.attackCooltime = 10

    def skillAttack(self, skillNum, monster):  # skillNum : 1,2,3
        print("player "+str(skillNum) + " 스킬 공격 사용")
        while self.attackCooltime > 0:
            self.mp -= 10 * skillNum
            monster.attacked(self.attackPower * skillNum)
            self.attackCooltime -= 1

    def normalAttack(self, monster):
        print("player 기본 공격 사용")
        while self.attackCooltime > 0:
            self.stem -= 10
            monster.attacked(self.attackPower)
            self.attackCooltime -= 1

    def attacked(self, attackedPower):
        self.hp -= attackedPower

    def result(self):
        return self.hp


class Monster:
    def __init__(self,hp, mp):
        self.hp = hp
        self.mp = mp
        self.attackPower = 2
        self.deffencePower = 1
        self.attackCooltime = 5

    def skillAttack(self, player):
        print("monster 스킬 공격 사용")
        while self.attackCooltime < 0:
            self.mp -= 5
            player.attacked(self.attackPower * 5)
            self.attackCooltime -= 1

    def normalAttack(self, player):
        print("monster 기본 공격 사용")
        while self.attackCooltime > 0:
            player.attacked(self.attackPower)
            self.attackCooltime -= 1

    def attacked(self, attackedPower):
        self.hp -= attackedPower

    def result(self):
        return self.hp

class GameManager:
    now = time.time()
    # player & monster list
    playerList = []
    monsterList = []
    def __init__(self):
        for i in range(10):
            hp = random.randrange(50, 200)
            mp = random.randrange(50, 100)
            stem = random.randrange(20, 50)
            self.playerList.append(Player(hp, mp, stem))
            self.monsterList.append(Monster(hp, mp))

    # fight!
    def run(self):
        while True:
            temp = random.choice([True,False])
            skillPlayer = random.choice([True,False])
            skillMonster = random.choice([True,False])
            playerNum = random.randrange(10)
            monsterNum = random.randrange(10)
            skillNum = random.randrange(3)
            if temp == True :
                # player 공격
                self.playerList[playerNum].normalAttack(self.monsterList[monsterNum])
                if skillPlayer == True :
                    self.playerList[playerNum].skillAttack(skillNum,self.monsterList[monsterNum])
                if self.playerList[playerNum].result() < 0 :
                    print("monster win")
                    break;

            elif temp == False :
                # monster 공격
                self.monsterList[monsterNum].normalAttack(self.playerList[playerNum])
                if skillMonster == True :
                    self.monsterList[monsterNum].skillAttack(self.playerList[playerNum])
                if self.monsterList[monsterNum].result() < 0 :
                    print("player win")
                    break;

Manager = GameManager()
Manager.run()