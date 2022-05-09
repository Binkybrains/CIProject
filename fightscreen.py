# fight screen program
import pygame
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 30

# game window
bottom_panel = 200
screen_width = 1400
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

# game variables
current_character = 1
total_characters = 2
action_cooldown = 0
wait_time = 90
attack = False
heal = False
heal_effect = 15
clicked = False
game_over = 0

# fonts
font = pygame.font.SysFont('Comic Sans', 35)

# colors
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
grey = (128, 128, 128)

# images
# background image
background_img = pygame.image.load('Hills Free (update 3.0).png').convert_alpha()
background_img = pygame.transform.scale(background_img, (1400, 550))
# panel image
panel_img = pygame.image.load('fightpanel1.png').convert_alpha()
panel_img = pygame.transform.scale(panel_img, (1400, 200))
# select bar image
cursor_image = pygame.image.load('cursor.png').convert_alpha()
cursor_image = pygame.transform.scale(cursor_image, (15, 20))
# fight image
fight_image = pygame.image.load('FightButton.png').convert_alpha()
fight_image = pygame.transform.scale(fight_image, (150, 75))
# Heal image
heal_image = pygame.image.load('HealButton.png').convert_alpha()
heal_image = pygame.transform.scale(heal_image, (150, 75))
# hpbar image
hpbar_image = pygame.image.load('hpbar.png').convert_alpha()
hpbar_image = pygame.transform.scale(hpbar_image, (500, 41))
# victory image
victory_image = pygame.image.load('victory.png').convert_alpha()
victory_image = pygame.transform.scale(victory_image, (400, 100))
# defeat image
defeat_image = pygame.image.load('defeat.png').convert_alpha()
defeat_image = pygame.transform.scale(defeat_image, (380, 100))
# energybar image
energybar_image = pygame.image.load('hpbar.png').convert_alpha()
energybar_image = pygame.transform.scale(hpbar_image, (250, 41))
# run button
run_image = pygame.image.load('runButton.png').convert_alpha()
run_image = pygame.transform.scale(run_image, (147, 58))

# text functional
def drawText(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

# draw background image
def drawBackground():
    screen.blit(background_img, (0, 0))


# draw panel image
def drawPanel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    screen.blit(fight_image, (50, screen_height - bottom_panel + 100))
    screen.blit(heal_image, (500, screen_height - bottom_panel + 100))
    screen.blit(heal_image, (1200, screen_height - bottom_panel + 100))
    screen.blit(hpbar_image, (100, screen_height - bottom_panel + 49))
    screen.blit(hpbar_image, (800, screen_height - bottom_panel + 49))
    screen.blit(energybar_image, (225, screen_height - bottom_panel + 100))
    screen.blit(energybar_image, (925, screen_height - bottom_panel + 100))
    screen.blit(run_image, (20, 20))
    # show stats
    drawText(f'{Karole.name} HP: {Karole.hp}', font, red, 130, (screen_height - bottom_panel) + 25)
    drawText(f'{Linda.name} HP: {Linda.hp}', font, red, 1120, (screen_height - bottom_panel) + 25)


# character class
class Character():
    def __init__(self, x, y, name, max_hp, max_energy, strength, heals):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_energy = max_energy
        self.energy = 0
        self.start_heals = heals
        self.heals = heals
        self.strength = strength

        ###########################################################################
        #this is for animation
        self.action = 0 #0 = idle, 1 = attack, 2 = hurt, 3 = dead
        ###########################################################################

        self.alive = True
        # add animation list here in order to make characters non static
        # increment the number in the png file  with a for loop(we will have to make all characters have an animation file)
        # https://www.youtube.com/watch?v=hZGtgv6Hh40 this video goes over how to do it for the future
        img = pygame.image.load('Karole0.png')
        self.image = pygame.transform.scale(img, (100, 225))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    ##########################################################################
    def attack(self, target):
        #deal damage to opponent
        rand = random.randint(-3, 3)
        damage = self.strength + rand
        target.hp -= damage
        #check if target is dead
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        damage_text = DamageText(target.rect.centerx, target.rect.y - 20, str(damage), red)
        damage_text_group.add(damage_text)
        #set up varibales for attack animation
        #self.action = 1
    ##########################################################################
    def specialAttack(self, target):
        rand = random.randint(-3, 3)
        damage = self.strength + rand + 10
        target.hp -= damage
        # check if target is dead
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        damage_text = DamageText(target.rect.centerx, target.rect.y - 20, str(damage), red)
        damage_text_group.add(damage_text)

    def draw(self):
        screen.blit(self.image, self.rect)

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        #update new health
        self.hp = hp
        # calc ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 442, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 442 * ratio, 20))

class EnergyBar():
    def __init__(self, x, y, energy, max_energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.max_energy = max_energy

    def draw(self, energy):
        #update new energy
        self.energy = energy
        # calc ratio
        ratio = self.energy / self.max_energy
        pygame.draw.rect(screen, grey, (self.x, self.y, 221, 20))
        pygame.draw.rect(screen, yellow, (self.x, self.y, 221 * ratio, 20))

###
###

class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        #move damage text
        self.rect.y -= 1
        # delete text after time
        self.counter += 1
        if self.counter > 25:
            self.kill()


damage_text_group = pygame.sprite.Group()

# define characters and stats
Karole = Character(250, 405, 'Karole', 30, 20, 5, 3)
Linda = Character(1150, 405, 'Linda', 20, 20, 6, 1)

# enemy_list = []
# can create characters above and add random enemies to this list in for more organisation and if we have a lot of enemies

# define hp bars
KaroleHpBar = HealthBar(130, screen_height - bottom_panel + 60, Karole.hp, Karole.max_hp)
LindaHpBar = HealthBar(828, screen_height - bottom_panel + 60, Linda.hp, Linda.max_hp)

# define energy bars
KaroleEnergyBar = EnergyBar(240, screen_height - bottom_panel + 111, Karole.energy, Karole.max_energy)
LindaEnergyBar = EnergyBar(940, screen_height - bottom_panel + 111, Linda.energy, Linda.max_energy)


run = True
while run:

    clock.tick(FPS)

    drawBackground()

    drawPanel()

    # draw actaul healthbar
    KaroleHpBar.draw(Karole.hp)
    LindaHpBar.draw(Linda.hp)

    # draw actaul energy bar
    KaroleEnergyBar.draw(Karole.energy)
    LindaEnergyBar.draw(Linda.energy)

    # draw characters
    Karole.draw()
    Linda.draw()

    # draw damage text
    damage_text_group.update()
    damage_text_group.draw(screen)
#####################################################################################
    # control character actions
    attack = False
    special = False
    runaway = False

    target = None
    heal = False

    fight_click = pygame.Rect(50, (screen_height - bottom_panel + 100), 150, 75)
    heal_click = pygame.Rect(500, (screen_height - bottom_panel + 100), 150, 75)
    special_click = pygame.Rect(240, (screen_height - bottom_panel + 111), 225, 20)
    runaway_click = pygame.Rect(20, 20, 147, 58)


    #make sure mouse is visible
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()

    if (fight_click.collidepoint(pos)):
        #hide mouse
        pygame.mouse.set_visible(False)
        #show cursor.png instead
        screen.blit(cursor_image, pos)
        if clicked == True:
            attack = True
            target = Linda

    if (heal_click.collidepoint(pos)):
        pygame.mouse.set_visible(False)
        screen.blit(cursor_image, pos)
        if clicked == True:
            heal = True

    if (special_click.collidepoint(pos)):
        pygame.mouse.set_visible(False)
        screen.blit(cursor_image, pos)
        if clicked == True:
            special = True
            target = Linda

    if (runaway_click.collidepoint(pos)):
        pygame.mouse.set_visible(False)
        screen.blit(cursor_image, pos)
        if clicked == True:
            runaway = True

    #show remaining potions
    drawText(str(Karole.heals), font, black, 630, screen_height - bottom_panel + 105)
    drawText(str(Linda.heals), font, black, 1330, screen_height - bottom_panel + 105)

    if game_over == 0:
        #character action
        if Karole.alive == True:
            if current_character == 1:
                action_cooldown += 1
                if action_cooldown >= wait_time:

                    #character action
                    #attack
                    if attack == True and target != None:
                        Karole.attack(target)
                        Karole.energy = Karole.energy + 10
                        if Karole.energy > Karole.max_energy:
                            Karole.energy = Karole.max_energy
                        current_character += 1
                        action_cooldown = 0
                    # special attack
                    if special == True and target != None and Karole.energy == Karole.max_energy:
                        Karole.specialAttack(target)
                        Karole.energy = 0
                        current_character += 1
                        action_cooldown = 0
                    # run away
                    if runaway == True:
                        game_over = -1
                    # Heal
                    if heal == True:
                        if Karole.heals > 0:
                            #see if it heals past max health
                            if Karole.max_hp - Karole.hp > heal_effect:
                                heal_amount = heal_effect
                            else:
                                heal_amount = Karole.max_hp - Karole.hp
                            Karole.hp += heal_amount
                            Karole.heals -= 1
                            damage_text = DamageText(Karole.rect.centerx, Karole.rect.y - 20, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            Karole.energy = Karole.energy + 10
                            if Karole.energy > Karole.max_energy:
                                Karole.energy = Karole.max_energy
                            current_character += 1
                            action_cooldown = 0
        else:
            game_over = -1

        # enemy action
        if current_character == 2:
            if Linda.alive == True:
                action_cooldown += 1
                if action_cooldown >= wait_time:
                    # check if linda needs heal
                    if (Linda.hp / Linda.max_hp) < 0.5 and Linda.heals > 0:
                        # see if it heals past max health
                        if Linda.max_hp - Linda.hp > heal_effect:
                            heal_amount = heal_effect
                        else:
                            heal_amount = Linda.max_hp - Linda.hp
                        Linda.hp += heal_amount
                        Linda.heals -= 1
                        damage_text = DamageText(Linda.rect.centerx, Linda.rect.y - 20, str(heal_amount), green)
                        damage_text_group.add(damage_text)
                        Linda.energy = Linda.energy + 10
                        if Linda.energy > Linda.max_energy:
                            Linda.energy = Linda.max_energy
                        current_character += 1
                        action_cooldown = 0
                    elif Linda.energy == Linda.max_energy:
                        Linda.specialAttack(Karole)
                        Linda.energy = 0
                        current_character += 1
                        action_cooldown = 0
                    else:
                        # attack
                        Linda.attack(Karole)
                        Linda.energy = Linda.energy + 10
                        if Linda.energy > Linda.max_energy:
                            Linda.energy = Linda.max_energy
                        current_character += 1
                        action_cooldown = 0
            else:
                # current_character += 1
                game_over = 1

        # once all characters take their turn then it will reset
        if current_character > total_characters:
            current_character = 1
######################################################################################
    if game_over != 0:
        if game_over == 1:
            screen.blit(victory_image, (500, 100))
        if game_over == -1:
            screen.blit(defeat_image, (520, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

############################################################################################
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False
########################################################################################
    pygame.display.update()

pygame.quit()
