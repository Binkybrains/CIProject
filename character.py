import pygame, sys
import random
from sprite import Sprite
from text import Text
from damagetext import DamageText


class Character(Sprite):
    def __init__(self, x, y, image, w, h, max_hp, max_energy, strength, screen, text_color, talkingHeads, heals, name):
        super().__init__(x, y, image, w, h, screen)
        self.__screen = screen
        self.__max_hp = max_hp
        self.__hp = max_hp
        self.__max_energy = max_energy
        self.__energy = 0
        self.__strength = strength
        self.__alive = True
        self.__start_heals = heals
        self.__heals = heals
        self.__textcolor = text_color
        self.__talkingHeads = talkingHeads
        self.__name = name


    # getters
    def getMaxHp(self):
        return self.__max_hp
    def getHp(self):
        return self.__hp
    def getMaxEnergy(self):
        return self.__max_energy
    def getEnergy(self):
        return self.__energy
    def getStrength(self):
        return self.__strength
    def getAlive(self):
        return self.__alive
    def getHeals(self):
        return self.__heals
    def getName(self):
        return self.__name


    # setters
    def setMaxHp(self, m):
        self.__max_hp = m
    def setHP(self, h):
        self.__hp = h
    def setMaxEnergy(self, m):
        self.__max_energy = m
    def setStrength(self, s):
        self.__strength = s
    def setAlive(self, b):
        self.__alive = b
    def setHeals(self, h):
        self.__heals = h
    def setEnergy(self, e):
        self.__energy = e

    # updates position of character
    def updatePos(self, pos):
        self.setX(pos[0])
        self.setY(pos[1])

    def attack(self, target):

        # deal damage to opponent
        rand = random.randint(-3,3)
        damage = self.__strength + rand
        target.setHP(target.getHp() - damage)

        # check if target is dead
        if target.getHp() < 1:
            target.setHP(0)
            target.setAlive(False)
        return DamageText(target.getX() + (target.getWidth()/2), target.getY() - 20, str(damage), (255,0,0))

    def specialAttack(self, target):
        rand = random.randint(-3, 3)
        damage = self.__strength + rand + 10
        target.setHP(target.getHp() - damage)

        if target.getHp() < 1:
            target.setHP(0)
            target.setAlive(False)

        return DamageText(target.getX() + (target.getWidth() / 2), target.getY() - 20, str(damage), (255, 0, 0))



    def drawHealth(self):
        # calc ratio
        ratio = self.__hp / self.__max_hp
        pygame.draw.rect(self.__screen, (255, 0, 0), (828, 610, 442, 20))
        pygame.draw.rect(self.__screen, (0, 255, 0), (828, 610, 442 * ratio, 20))

    def drawEnergyBar(self):
        # calc ratio
        ratio = self.__energy / self.__max_energy
        pygame.draw.rect(self.__screen, (128,128,128), (940, 661, 221, 20))
        pygame.draw.rect(self.__screen, (255, 255, 0), (940, 661, 221 * ratio, 20))

    def createText(self, y = 0, x = 0, boxW = 1400, boxH = 300, fontsize = 50):
        self.__charText = Text(self.__textcolor, self.__screen, x, y, boxW, boxH, fontsize)
        return self.__charText

    def createmessage(self, message):
        self.__charText.newMessage(message, True, self.__talkingHeads[0])

    def speak(self, volume):
        self.__charText.print_lines(volume)

    def textGetDone(self):
        return self.__charText.getDone()

    def textBox(self):
        self.__charText.text_box()
