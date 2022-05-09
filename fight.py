import pygame
from pygame.locals import *
from sprite import Sprite
from character import Character
from karole import Karole
from text import Text
import time
from damagetext import DamageText

class Fight():
    def __init__(self, fighters, screen, volume, cur_char = 0, act_cool = 0, wait_time = 90):
        self.__fighters = fighters
        self.__totChar = len(self.__fighters)
        self.__curChar = cur_char
        self.__actCool = act_cool
        self.__waitTime = wait_time
        self.__screen = screen
        self.__cursor = Sprite(0,0,"cursor.png", 25, 25, self.__screen)
        self.__target = None
        self.__fightToggle = True
        self.__attack = False
        self.__special = False
        self.__heal = False
        self.__healEffect = 15
        self.__fightB = Sprite(60, 650, "FightButton.png", 150, 75, self.__screen)
        self.__healB = Sprite(490, 650, "HealButton.png", 150, 75, self.__screen)
        self.__healBL = Sprite(1190, 650, "HealButton.png", 150, 75, self.__screen)
        self.__energybar = Sprite(225, 650, 'hpbar.png', 250, 41, self.__screen)
        self.__damage_text_group = pygame.sprite.Group()
        self.__count = 0
        self.__frames = 0
        self.__hoverF = False
        self.__hoverT = False
        self.__hoverE = False
        self.__volume = volume
        self.__hpbar_image = pygame.image.load('hpbar.png').convert_alpha()
        self.__energybar_image = pygame.transform.scale(self.__hpbar_image, (250, 41))

    def setFightToggle(self, b):
        self.__fightToggle = b
    def getFightToggle(self):
        return self.__fightToggle

    def updateFighters(self, fighters):
        self.__fighters = fighters

    def drawChars(self):
        self.__screen.blit(self.__energybar_image, (225, 650))
        self.__screen.blit(self.__energybar_image, (925, 650))
        for char in self.__fighters:
            char.draw()
            char.drawHealth()
            char.drawEnergyBar()
        font = pygame.font.Font(None, 35)
        imgC1 = font.render(str(self.__fighters[0].getHeals()), True, (0, 0, 0))
        imgC2 = font.render(str(self.__fighters[1].getHeals()), True, (0, 0, 0))
        self.__healB.draw()
        self.__fightB.draw()
        self.__healBL.draw()
        self.__screen.blit(imgC1, (620, 655))
        self.__screen.blit(imgC2, (1320, 655))

    def check_fight(self, volume):


        if self.__fighters[0].getAlive() == False:
            self.__fightToggle = False
            return False
        elif not True in [char.getAlive() for char in self.__fighters[1:]]:
            self.__fightToggle = False
            return True

        pos = pygame.mouse.get_pos()
        if self.__fightToggle:
            hover_sound = pygame.mixer.Sound("hoverbutton.mp3")
            click_sound = pygame.mixer.Sound("clickbutton.mp3")
            punch_sound = pygame.mixer.Sound("heavypunchsound.mp3")
            pygame.mixer.Sound.set_volume(hover_sound, volume)
            pygame.mixer.Sound.set_volume(click_sound, volume)
            pygame.mixer.Sound.set_volume(punch_sound, volume)


            self.__damage_text_group.update()
            self.__damage_text_group.draw(self.__screen)
            if self.__curChar == self.__totChar:
                self.__count += 1
                self.drawChars()
                pygame.display.update()
                if self.__count == 30:
                    if len(self.__LinesToRun) != 0:
                        self.__fighters[0].textBox()
                    self.__fightToggle = False
                    self.__count = 0
                    self.__curChar = 0

            else:

                if self.__fightB.getRect().collidepoint(pos):
                    if self.__hoverF == False:
                        pygame.mixer.Sound.play(hover_sound)
                    self.__hoverF = True
                    pygame.mouse.set_visible(False)
                    self.__cursor.setPos(pos)
                    self.__cursor.draw()
                    if self.__target == None:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                pygame.mixer.Sound.play(click_sound)
                                self.__target = self.__fighters[1]
                                self.__attack = True
                else:
                    pygame.mouse.set_visible(True)
                    self.__hoverF = False

                if self.__healB.getRect().collidepoint(pos):
                    pygame.mouse.set_visible(False)
                    self.__cursor.setPos(pos)
                    self.__cursor.draw()
                    if self.__hoverH == False:
                        pygame.mixer.Sound.play(hover_sound)
                    self.__hoverH = True
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            pygame.mixer.Sound.play(click_sound)
                            self.__heal = True
                else:
                    pygame.mouse.set_visible(True)
                    self.__hoverH = False


                if self.__energybar.getRect().collidepoint(pos):
                    pygame.mouse.set_visible(False)
                    self.__cursor.setPos(pos)
                    self.__cursor.draw()
                    if not self.__hoverE:
                        pygame.mixer.Sound.play(hover_sound)
                        self.__hoverE = True
                    if self.__target == None and self.__curChar == 0:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONUP:
                                pygame.mixer.Sound.play(click_sound)
                                self.__target = self.__fighters[1]
                                self.__special = True
                                self.__attack = True
                else:
                    pygame.mouse.set_visible(True)
                    self.__hoverE = False

                for index, char in enumerate(self.__fighters):

                    if char.getAlive():
                        if self.__curChar == index:
                            self.__actCool += 1
                            if self.__actCool >= self.__waitTime:
                                # char action
                                # attack
                                if (index == 0):
                                    if self.__heal and char.getHeals() > 0:
                                        if char.getMaxHp() - char.getHp() > self.__healEffect:
                                            heal_amount = self.__healEffect
                                        else:
                                            heal_amount = char.getMaxHp() - char.getHp()
                                        char.setHP(char.getHp() + heal_amount)
                                        char.setHeals(char.getHeals() - 1)
                                        damage = DamageText(char.getX() + (char.getWidth()/2), char.getY() - 20, str(heal_amount), (0, 255, 0))
                                        self.__damage_text_group.add(damage)
                                        self.__heal = False
                                        self.__curChar += 1
                                        self.__actCool = 0
                                        char.setEnergy(char.getEnergy() + 10)
                                        if char.getEnergy() > char.getMaxEnergy():
                                            char.setEnergy(char.getMaxEnergy())

                                    elif self.__attack and  self.__target != None:


                                        if (self.__special and char.getEnergy() != char.getMaxEnergy()):
                                            self.__attack = False
                                            self.__special = False
                                            self.__target = None
                                        else:
                                            self.__frames += 1
                                            if self.__frames == 1:
                                                pygame.mixer.Sound.play(punch_sound)
                                                self.__target.setImg((self.__target.getName() + "_tinted_sprite.png"))
                                            if self.__frames >= 20:
                                                if self.__frames in [20, 30, 40, 50, 60]:
                                                    self.__target.setAlpha(0)
                                                elif self.__frames in [25, 35, 45, 55, 65]:
                                                    self.__target.setAlpha(255)
                                                elif self.__frames >= 70:
                                                    if self.__special:
                                                        damage = char.specialAttack(self.__target)
                                                        char.setEnergy(0)
                                                    else:
                                                        damage = char.attack(self.__target)
                                                    self.__damage_text_group.add(damage)
                                                    self.__target.setImg((self.__target.getName() + "_stationary.png"))
                                                    self.__target = None
                                                    self.__attack = False
                                                    self.__curChar += 1
                                                    self.__actCool = 0
                                                    self.__frames = 0
                                                    if self.__special == False:
                                                        char.setEnergy(char.getEnergy() + 10)
                                                        if char.getEnergy() > char.getMaxEnergy():
                                                            char.setEnergy(char.getMaxEnergy())
                                                    else:
                                                        self.__special = False



                                elif index != 0:
                                    if (char.getHp() / char.getMaxHp()) < 0.5 and char.getHeals() > 0:
                                        if char.getMaxHp() - char.getHp() > self.__healEffect:
                                            heal_amount = self.__healEffect
                                        else:
                                            heal_amount = char.getMaxHp() - char.getHp()
                                        char.setHP(char.getHp() + heal_amount)
                                        char.setHeals(char.getHeals() - 1)
                                        damage = DamageText(char.getX() + (char.getWidth()/2), char.getY() - 20, str(heal_amount), (0, 255, 0))
                                        self.__damage_text_group.add(damage)
                                        self.__curChar += 1
                                        self.__actCool = 0
                                        char.setEnergy(char.getEnergy() + 10)
                                        if char.getEnergy() > char.getMaxEnergy():
                                            char.setEnergy(char.getMaxEnergy())
                                    else:

                                        self.__frames += 1
                                        if self.__frames == 1:
                                            pygame.mixer.Sound.play(punch_sound)
                                            self.__fighters[0].setImg("tinted_karole_sprite.png")
                                            pass
                                        if self.__frames >= 20:
                                            if self.__frames in [20, 30, 40, 50, 60]:
                                                self.__fighters[0].setAlpha(0)
                                            elif self.__frames in [25, 35, 45, 55, 65]:
                                                self.__fighters[0].setAlpha(255)
                                            elif self.__frames >= 70:
                                                if char.getEnergy() == char.getMaxEnergy():
                                                    char.setEnergy(0)
                                                    damage = char.specialAttack(self.__fighters[0])
                                                    self.__special = True
                                                else:
                                                    damage = char.attack(self.__fighters[0])
                                                self.__damage_text_group.add(damage)
                                                self.__fighters[0].setImg("Karole_walk1.png")
                                                self.__target = None
                                                self.__attack = False
                                                self.__curChar += 1
                                                self.__actCool = 0
                                                self.__frames = 0
                                                if self.__special == False:
                                                    char.setEnergy(char.getEnergy() + 10)
                                                    if char.getEnergy() > char.getMaxEnergy():
                                                        char.setEnergy(char.getMaxEnergy())
                                                else:
                                                    self.__special = False

                    else:
                        self.__curChar += 1
        else:
            self.print_line()

    def create_lines(self, lines_to_run):
        self.__LinesToRun = lines_to_run
        if len(self.__LinesToRun) != 0:
            for i in range(len(self.__fighters)):
                self.__fighters[i].createText(450, 0)
            self.__narText = Text((0,0,0), self.__screen, 450, 0, 1400, 300)
            if self.__LinesToRun[0][0] == "N":
                self.__narText.newMessage(self.__LinesToRun[2])
            else:
                self.__fighters[int(self.__LinesToRun[0][0])].createmessage(self.__LinesToRun[2])

    def create_new_line(self):
        if len(self.__LinesToRun) != 0:
            if len(self.__LinesToRun[0]) == 1:
                self.__LinesToRun = []
            else:
                self.__LinesToRun[0] = self.__LinesToRun[0][1:]
                self.__LinesToRun[1] = self.__LinesToRun[1][1:]
                self.__LinesToRun.pop(2)
        if len(self.__LinesToRun) != 0:
            if self.__LinesToRun[0][0] == "N":
                self.__narText.newMessage(self.__LinesToRun[2])
            else:
                self.__fighters[int(self.__LinesToRun[0][0])].createmessage(self.__LinesToRun[2])

    def print_line(self):
        pygame.mouse.set_visible(False)
        if len(self.__LinesToRun) != 0:
            if self.__LinesToRun[0][0] == "N":
                if self.__narText.getDone():
                    self.create_new_line()
                    if len(self.__LinesToRun[1]) != 1:
                        if self.__LinesToRun[1][0] != self.__LinesToRun[1][1]:
                            self.__fightToggle = True
                    else:
                        self.__fightToggle = True
                else:
                    self.__narText.print_lines(self.__volume)

            elif self.__fighters[int(self.__LinesToRun[0][0])].textGetDone():
                self.create_new_line()
                if len(self.__LinesToRun) != 0:
                    if len(self.__LinesToRun[1]) != 1:
                        if self.__LinesToRun[1][0] != self.__LinesToRun[1][1]:
                            self.__fightToggle = True
                    else:
                        self.__fightToggle = True
                else:
                    self.__fightToggle = True
            else:
                self.__fighters[int(self.__LinesToRun[0][0])].speak(self.__volume)
        else:
            self.__fightToggle = True
