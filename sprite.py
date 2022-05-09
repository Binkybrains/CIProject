import pygame, sys
from pygame.locals import *

#draws sprites
class Sprite:

    #initizes proper attributes
    def __init__(self, posx, posy, img, w, h, screen):
        self.__x = posx
        self.__y = posy
        self.__image = img
        self.__width = w
        self.__height = h
        self.__screen = screen
        self.__alpha = 255
        try:
            image = pygame.image.load(self.__image).convert_alpha()
            self.__originW = image.get_rect().width
            self.__originH = image.get_rect().height
            self.__scaleW = float(self.__width)/self.__originW
            self.__scaleH = float(self.__height)/self.__originH
        except:
            pass

    # getters
    def getImg(self):
        return self.__image
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getRect(self):
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)

    # setters
    def setImg(self, img):
        self.__image = img
        image = pygame.image.load(self.__image).convert_alpha()
        self.setHeight(int(image.get_rect().height * self.__scaleH))
        self.setWidth(int(image.get_rect().width * self.__scaleW))
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def setWidth(self, w):
        self.__width = w
    def setHeight(self, h):
        self.__height = h
    def setPos(self, t):
        self.__x = t[0]
        self.__y = t[1]
    def setAlpha(self, a):
        self.__alpha = a

    # gets the position of the sprite
    def getpos(self):
        return (self.__x, self.__y)

    # draws the sprite to the screen
    def draw(self):
        image = pygame.image.load(self.__image).convert_alpha()
        image = pygame.transform.scale(image, (self.__width, self.__height))
        image.set_alpha(self.__alpha)
        self.__screen.blit(image, self.getpos())


