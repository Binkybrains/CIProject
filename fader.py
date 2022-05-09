import pygame
from itertools import cycle
class Fader:
    def __init__(self, scenes):
        self.scenes = cycle(scenes)
        self.scene = next(self.scenes)
        self.fading = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))

    #Fading IN means the veil is fading in, OUT means the next screen is fading in/veil fades OUT
    def next(self):
        if self.fading == "IN":
            self.fading = "OUT"
            self.alpha = 0
        else:
            self.fading = "IN"
            self.alpha = 255

    #The scene is drawing
    def draw(self, screen):
        self.scene.draw(screen)
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))

    #The black veil in front of the graphics is updating to be more and more transparent or less and less
    def update(self, dt):
        self.scene.update(dt)
        if self.fading == "OUT":
            self.alpha += 8
            if self.alpha >= 255:
                self.fading = "IN"
                self.scene = next(self.scenes)
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = "OUT"
