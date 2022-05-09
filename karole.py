import pygame, sys
from character import *

class Karole(Character): #Class is responsible for the main character of the game inherets from Character class
    def __init__(self, x, y, w, h, max_hp, max_energy, strength, heals, screen):
        super().__init__(x, y, 'Karole_walk1.png', w, h, max_hp, max_energy, strength, screen, (255, 0, 0), ["karoleHEAD.png"], heals, "karole")
        self.__screen = screen
        self.__alive = True
        self.__imagesR = ['Karole_walk1.png', 'Karole_walk2.png', 'Karole_walk3.png', 'Karole_walk4.png', 'Karole_walk5.png', 'Karole_walk6.png']
        self.__imagesL = ['Karole_walk7.png', 'Karole_walk8.png', 'Karole_walk9.png', 'Karole_walk10.png', 'Karole_walk11.png', 'Karole_walk12.png']
        self.__frameNUM = 0
        self.__dir = 'r'

    # checks if the charcter as moved
    def check_move(self, listOBJ=[]): #checks Karole's movements

        pressed = pygame.key.get_pressed()
        walked = False
        currentR = [i for i in range(6) if self.__imagesR[i] == self.getImg()]
        currentL = [i for i in range(6) if self.__imagesL[i] == self.getImg()]

        # down
        if pressed[pygame.K_s]:
            walked = True
            if self.getY() < (750 - self.getHeight()): #if she has room on the screen to move moves her down
                self.setY(self.getY() + 5)
                if self.__frameNUM == 15:
                    self.__frameNUM = 0
                    if len(currentR) != 0 and currentR[0] != 5:
                        self.setImg(self.__imagesR[currentR[0] + 1])
                    else:
                        self.setImg(self.__imagesR[0])
                else:
                    self.__frameNUM += 1
                if len(self.returnTouching(listOBJ)) != 0: #if she is colliding then it undos any movemnt to mimic her standing still
                    self.setY(self.getY() - 5)
                    if len(self.returnTouching(listOBJ)) != 0:
                        self.setY(self.getY() + 5)

        # right
        if pressed[pygame.K_d]:
            walked = True
            if self.getX() < (1400 - self.getWidth()):
                self.setX(self.getX() + 5)
                if self.__frameNUM == 15:
                    self.__frameNUM = 0
                    if len(currentR) != 0 and currentR[0] != 5:
                        self.setImg(self.__imagesR[currentR[0] + 1])
                    else:
                        self.setImg(self.__imagesR[0])
                else:
                    self.__frameNUM += 1
                if len(self.returnTouching(listOBJ)) != 0:
                    self.setX(self.getX() - 5)
                    if len(self.returnTouching(listOBJ)) != 0:
                        self.setX(self.getX() + 5)


        # up
        if pressed[pygame.K_w]:
            walked = True
            if self.getY() > 200:
                self.setY(self.getY()-5)
                if self.__frameNUM == 15:
                    self.__frameNUM = 0
                    if len(currentL) != 0 and currentL[0] != 5:
                        self.setImg(self.__imagesL[currentL[0] + 1])
                    else:
                        self.setImg(self.__imagesL[0])
                else:
                    self.__frameNUM += 1
                if len(self.returnTouching(listOBJ)) != 0:
                    self.setY(self.getY() + 5)
                    if len(self.returnTouching(listOBJ)) != 0:
                        self.setY(self.getY() - 5)

        # left
        if pressed[pygame.K_a]:
            walked = True
            if self.getX() > 0:
                self.setX(self.getX()-5)
                if self.__frameNUM == 15:
                    self.__frameNUM = 0
                    if len(currentL) != 0 and currentL[0] != 5:
                        self.setImg(self.__imagesL[currentL[0] + 1])
                    else:
                        self.setImg(self.__imagesL[0])
                else:
                    self.__frameNUM += 1
                if len(self.returnTouching(listOBJ)) != 0:
                    self.setX(self.getX() + 5)
                    if len(self.returnTouching(listOBJ)) != 0:
                        self.setX(self.getX() - 5)

        if not walked: #stopping animation
            if self.__frameNUM >= 7:
                self.__frameNUM = 0
                if len(currentR) == 0:
                    if currentL[0] != 0:
                        self.setImg(self.__imagesL[currentL[0] - 1])
                else:
                    if currentR[0] != 0:
                        self.setImg(self.__imagesR[currentR[0] - 1])
                    else:
                        self.__frameNUM += 1
            else:
                self.__frameNUM += 1


    def drawHealth(self):

        # calc ratio
        ratio = self.getHp() / self.getMaxHp()
        pygame.draw.rect(self.__screen, (255, 0, 0), (130, 610, 442, 20))
        pygame.draw.rect(self.__screen, (0, 255, 0), (130, 610, 442 * ratio, 20))

    def drawEnergyBar(self):

        # calc ratio
        ratio = self.getEnergy() / self.getMaxEnergy()
        pygame.draw.rect(self.__screen, (128, 128, 128), (240, 661, 221, 20))
        pygame.draw.rect(self.__screen, (255, 255, 0), (240, 661, 221 * ratio, 20))

    def returnTouching(self, list_objects):
        objects_touched = []
        for i in range(len(list_objects)):

            # if the karole is touching the object
            rectK = self.getRect()
            rectO = pygame.Rect(list_objects[i].getX(), list_objects[i].getY(), list_objects[i].getWidth(), list_objects[i].getHeight())
            if isinstance(list_objects[i], Character):
                if self.getY() == list_objects[i].getY():
                    if rectK.colliderect(rectO):
                        objects_touched.append(list_objects[i])
                if self.getY() < list_objects[i].getY() and (self.getX() < list_objects[i].getX() + list_objects[i].getWidth() and self.getX() >= list_objects[i].getX() - self.getWidth()):
                    list_objects[i].draw()
            elif rectK.colliderect(rectO):
                objects_touched.append(list_objects[i])
        return objects_touched
