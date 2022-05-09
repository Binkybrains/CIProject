import pygame, sys
from pygame.locals import *
from sprite import Sprite

class Text:

    #initilized needed attributes
    def __init__(self, color, screen, x, y, boxW = 1400, boxH = 300, fontsize = 40):
        self.__color = color
        self.__x = x
        self.__y = y
        self.__screen = screen
        self.__boxW = boxW
        self.__boxH = boxH
        self.__fontsize = fontsize
        self.__done = False
        self.__frameNUM = 1

    def getVolume(self):
        return self.__volume

    def newMessage(self, text, th=False, img = ''):
        # creates textbox and starting positions of the text
        self.text_box()
        self.__px = self.__x + 10
        self.__py = self.__y + 10
        self.__done = False

        # initlizes font and enter key
        self.__font = pygame.font.Font(None, self.__fontsize)
        self.__enter = Sprite(self.__boxW + self.__x - 45, self.__y + self.__boxH - 45, "enter.png", 40, 40,
                              self.__screen)

        # splits text by word
        self.__text = text
        self.__text = [i for j in self.__text.split() for i in (j, ' ')][:-1]

        # weather or not text is being printed
        self.__toggle = True
        self.__textOBJ = Sprite(self.__x, self.__y, '', self.__boxW, self.__boxH, self.__screen)

        # creates an image of a word
        self.__word = self.__font.render(text[0], True, self.__color)
        self.__th = th
        self.__currentL = 0
        if self.__th:
            self.__talkinH = Sprite(self.__x + 10, self.__y + 10, img, 200,280, self.__screen)
            self.__px = self.__x + 220


    def getTextOBJ(self):
        return self.__textOBJ

    def getDone(self):
        return self.__done

    #creates a text box for the text to sit on top of
    def text_box(self):
        pygame.draw.rect(self.__screen, (0,0,0), (self.__x, self.__y, self.__boxW, self.__boxH))

    #prints the text on the text box
    def print_lines(self, volume):
        self.__volume = volume
        textSound = pygame.mixer.Sound("textscroll.mp3")
        if volume - 0.2 <= 0:
            pygame.mixer.Sound.set_volume(textSound, volume)
        else:
            pygame.mixer.Sound.set_volume(textSound, volume-0.2)
        headlen = 0
        if self.__th:
            self.__talkinH.draw()
            headlen = self.__talkinH.getWidth()

        if len(self.__text) != 0:
            if self.__currentL <= len(self.__text[0]) - 1:
                l = self.__text[0][self.__currentL]
                if l == '=':
                    self.__currentL += 1
                    self.__px = self.__x + 20 + headlen
                    self.__py = self.__y + 10
                    self.__enter.draw()
                    self.__toggle = False
                    pygame.display.update()
        if len(self.__text) != 0 and self.__toggle:

            # goes letter by letter in the top word of the word list
            if self.__currentL <= len(self.__text[0])-1:
                self.__frameNUM += 1

                # waits to draw letter
                if self.__frameNUM % 2 == 0:

                    l = self.__text[0][self.__currentL]
                    let = self.__font.render(l, True, self.__color)
                    self.__screen.blit(let, (self.__px, self.__py))
                    let_rect = let.get_rect()
                    # updates current position
                    self.__px += let_rect.width + 5
                    self.__currentL += 1
                    if self.__frameNUM % 4 == 0:
                        pygame.mixer.Sound.play(textSound)
                    pygame.display.update()
            else:
                self.__currentL = 0

                #removes word at top of word list once word is displayed
                self.__text.pop(0)

                if len(self.__text) != 0:

                    #creates a new word and gets its bounding rectangle
                    word = self.__font.render(self.__text[0], True, self.__color)
                    rect = word.get_rect()

                    #If there is no space on the line and no space for new lines, show the enter button and turns off toggle
                    if (self.__py + rect.height * 2) > (self.__y + self.__boxH - 15) and (self.__px + rect.width * 2) > (self.__x + self.__boxW-65):
                        self.__px = self.__x + 10 + headlen
                        self.__py = self.__y + 10
                        self.__enter.draw()
                        self.__toggle = False
                        pygame.display.update()

                    #If there is no room for the next word on the current line, moves the x to its starting position and y down a line
                    elif (self.__py + rect.height*2) <= (self.__y+self.__boxH-15) and not (self.__px + rect.width) <= (self.__x + self.__boxW-25):
                        self.__px = self.__x + 10 + headlen
                        self.__py += rect.height + 5

        #if the toggle is false, or there are no more words, draw enter
        else:
            self.__enter.draw()
            self.__toggle = False
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:



                #if the return key is pressed
                if event.key == K_RETURN:

                    #if the toggle is false (return key has been drawn on screen)
                    if self.__toggle == False:
                        if self.__th:
                            self.text_box()
                        else:
                            self.text_box()
                        #creates a new text box, and lets the screen draw more words
                        self.__toggle = True
                        if len(self.__text) == 0:
                            self.__done = True
                            self.__toggle = False

            if event.type == QUIT:
                pygame.quit()
                sys.exit()





