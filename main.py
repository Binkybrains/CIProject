import pygame
import sys
from character import Character
from fight import Fight
from karole import Karole
from pygame.locals import *
from text import Text
from sprite import Sprite

def credits():
    global clock, DISPLAYSURF

    victory = Sprite(0, 0, 'credit_screen.png', 1400, 750, DISPLAYSURF)
    while True:
        victory.draw()
        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(30)
        pygame.display.update()

def game_over():
    global clock, DISPLAYSURF, volume

    defeat = Sprite(520, 100, 'defeat.png', 380, 100, DISPLAYSURF)
    defeat.draw()
    death_sound = pygame.mixer.Sound("deathsound.mp3")
    pygame.mixer.Sound.play(death_sound)
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 450)
    narText.newMessage("Restart fight?")
    curtext = 0

    while True:
        if narText.getDone():
            curtext = choice('YES', 'NO', 0, (300, 500), (1000, 500), 0, 450)
            if curtext == 1:
                narText.newMessage("Restart fight?")
            elif curtext == 2:
                return
        else:
            narText.print_lines(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)






def after_brenda():
    global clock, DISPLAYSURF, karole, stacy, brenda, debbie, linda, brienne, volume

    DISPLAYSURF.fill((15, 0, 0))

    karole.updatePos((500, 300))
    karole.setImg('Karole_walk1.png')
    brenda.updatePos((800, 300))
    brenda.setImg('Brenda_stationary.png')
    debbie.updatePos((200, 300))
    debbie.setImg('Debbie_stationary_Right.png')
    brienne.updatePos((1100, 300))
    brienne.setImg('Brieanne-Teigh_stationary.png')
    stacy.updatePos((350, 450))
    stacy.setImg('Stacy_stationary_right.png')
    linda.updatePos((950, 450))
    linda.setImg('Linda_stationary.png')

    alphaList = [karole, stacy, brenda, debbie, linda, brienne]

    curtext = 0
    karole.createText()
    brenda.createText()
    debbie.createText()
    brienne.createText()
    stacy.createText()
    linda.createText()
    brenda.createmessage("I can’t believe this has happened! I’m meant to always be the PTA president not you! Debbie! Come take this little cheater away! I’m not dealing with this right now.")
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 0)
    narText.newMessage("a")
    pygame.mouse.set_visible(False)

    debbie.setAlpha(0)
    brienne.setAlpha(0)
    stacy.setAlpha(0)
    linda.setAlpha(0)

    while True:
        DISPLAYSURF.set_clip((0, 300, 1400, 750))
        DISPLAYSURF.fill((10,0,0))
        DISPLAYSURF.set_clip((0, 0, 1400, 750))

        karole.draw()
        brenda.draw()
        debbie.draw()
        brienne.draw()
        stacy.draw()
        linda.draw()


        if curtext == 0:
            if brenda.textGetDone():
                curtext = 1
                debbieAlpha = 0
            else:
                brenda.speak(volume)

        elif curtext == 1:
            if debbieAlpha < 255:
                debbieAlpha += 1
                debbie.setAlpha(debbieAlpha)
            else:
                curtext = 2
                debbie.createmessage("No way, Brenda-Simone. I’m done being pushed around by you. Find another person to be your goon. Me and my kid are done playing by your rules.")

        elif curtext == 2:
            if debbie.textGetDone():
                curtext = 3
                brenda.createmessage("Fine! I don’t even need you anyway. Hope your kid has fun getting suspended without me there to bribe the principal. Brieanne-Teigh! Take Karole back to the kitchens, I think a hairnet and garbage duty for 3 months is calling her name.")
            else:
                debbie.speak(volume)

        elif curtext == 3:
            if brenda.textGetDone():
                curtext = 4
                brienneAlpha = 0
            else:
                brenda.speak(volume)

        elif curtext == 4:
            if brienneAlpha < 255:
                brienneAlpha += 1
                brienne.setAlpha(brienneAlpha)
            else:
                curtext = 5
                brienne.createmessage("Brenda-Simone… we like Karole now! She’s told me that she’ll endorse my great aunt’s line of recyclable shoes upcycled from cardboard boxes when she’s PTA president! This is a great opportunity! I think I might even be able to squeeze in an addendum about the fact they disintegrate in water this time!")

        elif curtext == 5:
            if brienne.textGetDone():
                curtext = 6
                brenda.createmessage("Brieanne-Teigh, you’re utterly useless as always. Stacy! Finish this for once and for all would you?")
            else:
                brienne.speak(volume)

        elif curtext == 6:
            if brenda.textGetDone():
                curtext = 7
                stacyAlpha = 0
            else:
                brenda.speak(volume)

        elif curtext == 7:
            if stacyAlpha < 255:
                stacyAlpha += 1
                stacy.setAlpha(stacyAlpha)
            else:
                curtext = 8
                stacy.createmessage("Sorry, Brenda-Simone, but I only answer to the PTA president, which you clearly are not anymore. But if you’re looking to stay involved I hear there’s an opening in the kitchen and garbage cleaning crew apparently!")
                lindaAlpha = 0

        elif curtext == 8:
            if stacy.textGetDone():
                linda.createmessage("Yeah, get out of here old news! And take those raggedy split ends with you!")
                curtext = 9
            else:
                stacy.speak(volume)
                if lindaAlpha < 255:
                    lindaAlpha += 1
                    linda.setAlpha(lindaAlpha)

        elif curtext == 9:
            if linda.textGetDone():
                curtext = 10
                karole.createmessage("Finally! I made it to the top! Goodbye Brenda-Simone, there’s a new PTA president sitting on the throne!")
            else:
                linda.speak(volume)

        elif curtext == 10:
            if karole.textGetDone():
                curtext = 11
                charAlpha = 255
            else:
                karole.speak(volume)

        elif curtext == 11:
            if charAlpha > 0:
                charAlpha -= 1
                for char in alphaList:
                    char.setAlpha(charAlpha)
            else:
                credits()

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)




def after_stacy():
    global clock, DISPLAYSURF, karole, stacy, brenda, volume

    hover01 = False
    hover02 = False
    DISPLAYSURF.fill((255, 255, 255))
    background = Sprite(0, 0, "PTA_meeting_background-1.png.png", 1400, 750, DISPLAYSURF)
    karole.updatePos((600, 400))
    karole.setImg('Karole_walk1.png')
    stacy.updatePos((1200, 400))
    stacy.setImg('Stacy_stationary.png')
    brenda.setImg('Brenda_stationary copy.png')
    curtext = 0
    karole.createText()
    stacy.createText()
    brenda.createText()
    brenda.updatePos((100, 300))
    stacy.createmessage("Wow. That was amazing. Maybe I underestimated you, Karole. I’m rooting for you against Brenda-Simone. You know, I think that we could make a good team. Here take my card, if you win this next fight, give me a call. I think those skills of yours might be transferable to a career a little bit bigger than being the president of some little PTA. Okay?")
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 0)
    narText.newMessage("a")
    listOBJ = [stacy, narText.getTextOBJ()]
    pygame.mouse.set_visible(False)
    brendaT = False
    brenda.setAlpha(0)

    while True:
        if curtext in [3]:
            background.draw()
        else:
            DISPLAYSURF.set_clip((0, 300, 1400, 750))
            background.draw()
            DISPLAYSURF.set_clip((0, 0, 1400, 750))

        stacy.draw()
        brenda.draw()
        karole.draw()
        karole.check_move(listOBJ)
        karole.returnTouching(listOBJ)

        if curtext == 0:
            if stacy.textGetDone():
                curtext = choice("Okay sure!", "No way!", 0, (50, 60), (50, 150))
                if curtext in [1,2]:
                    stacy.createmessage("Oh look! There Brenda-Simone is now! Just remember your training and stay strong. And maybe come find me afterwards, even if you lose. See you later, hotshot.")
                    brendaAlpha = 0
                    listOBJ.append(brenda)
            else:
                stacy.speak(volume)

        elif curtext in [1,2]:
            pygame.mouse.set_visible(False)
            if stacy.textGetDone():
                curtext = 3
            else:
                stacy.speak(volume)
                if brendaAlpha < 255:
                    brendaAlpha += 1
                    brenda.setAlpha(brendaAlpha)

        elif curtext == 3:
            brendaT = karole.getX() <= brenda.getX() + 130 and karole.getY() + 30 >= brenda.getY()

        elif curtext == 4:
            if brenda.textGetDone():
                karole.createmessage("I’m not afraid of you! You’ve been the unchecked tyrant over this PTA for far too long! It was only a matter of time before someone like me came along and finally had the guts and the skills to take you out!")
                curtext = 5
            else:
                brenda.speak(volume)

        elif curtext == 5:
            if karole.textGetDone():
                brenda.createmessage("Well let’s stop talking and get to it! The meeting is starting in 15 minutes and I don’t have time to waste when I could be kicking you to next Monday. Linda! I hope your eyes are wide open. I want you to watch as I crush your newest champion.")
                curtext = 6
            else:
                karole.speak(volume)

        elif curtext == 6:
            if brenda.textGetDone():
                narText.newMessage("Initiate fight with Brenda-Simone?")
                curtext = 7
            else:
                brenda.speak(volume)

        elif curtext == 7:
            if narText.getDone():
                curtext = choice('YES', 'NO', 7, (300, 50), (1000, 50))
                if curtext == 8:
                    brenda.createmessage("Guess you didn’t have it in you after all. What are you scared? Afraid of being sent back to the corner where you belong. You wouldn’t have won this fight anyway.")
                    pygame.mouse.set_visible(False)
                    curtext = 6
                elif curtext == 9:
                    brendaFight()
            else:
                narText.print_lines(volume)



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_volume(event)
                if event.key == K_e:
                    if curtext == 3:
                        if brendaT:
                            listOBJ.append(narText.getTextOBJ())
                            brenda.createmessage("What’s this? A little piece of trash seems to have flown its way in front of my throne. Brieanne-Teigh! Stacy! I can’t believe you would allow this poor excuse of a mother to even interact with me! This is why I’m so needed around here and why I’m on my 5th consecutive unchallenged term as PTA president. You all so clearly need my help and the structure I give this organization just by my very being alive.")
                            curtext = 4
                            brendaT = False

        pygame.display.update()
        clock.tick(60)


def after_brieanne():
    global clock, DISPLAYSURF, karole, brienne, stacy, volume

    hover01 = False
    hover02 = False
    DISPLAYSURF.fill((255, 255, 255))
    background = Sprite(0, 0, "PTA_meeting_background-1.png.png", 1400, 750, DISPLAYSURF)
    karole.updatePos((600, 400))
    karole.setImg('Karole_walk1.png')
    brienne.updatePos((1200, 400))
    brienne.setImg('Brieanne-Teigh_stationary.png')
    stacy.setImg('Stacy_stationary_right.png')
    curtext = 0
    karole.createText()
    brienne.createText()
    stacy.createText()
    brienne.createmessage("That was so much fun! I’m so happy we got to share that moment together! Are you up for a little post-fight deep breathing centered meditation?")
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 0)
    narText.newMessage("a")
    listOBJ = [brienne, narText.getTextOBJ()]
    pygame.mouse.set_visible(False)
    stacyT = False
    stacy.setAlpha(0)

    while True:
        if curtext in [5]:
            background.draw()
        else:
            DISPLAYSURF.set_clip((0, 300, 1400, 750))
            background.draw()
            DISPLAYSURF.set_clip((0, 0, 1400, 750))

        brienne.draw()
        stacy.draw()
        karole.draw()
        karole.check_move(listOBJ)
        karole.returnTouching(listOBJ)

        if curtext == 0:
            if brienne.textGetDone():
                curtext = choice("Please no.", "Maybe another time...", 0, (50, 60), (50, 150))
                if curtext in [1,2]:
                    brienne.createmessage("That’s okay! We can touch base and circle back to this conversation another time! If you had a good time with me, the next person you need to go see is Stacy, the powerhouse in the suit! She’s always a good time and has a great record in divorce court FYI. I hope you and her can become great friends, just like us! Try to not get your face beaten in!")
                    stacyAlpha = 0
                    listOBJ.append(stacy)
            else:
                brienne.speak(volume)

        elif curtext in [1,2]:
            pygame.mouse.set_visible(False)
            if brienne.textGetDone():
                curtext = choice("Thanks...I guess.", "Let’s do this!", 2, (50, 60), (50, 150))
                if curtext in [3,4]:
                    brienne.createmessage("That's the spirit hun!! You're doing great sweetie!")
            else:
                brienne.speak(volume)
                if stacyAlpha < 255:
                    stacyAlpha += 1
                    stacy.setAlpha(stacyAlpha)

        elif curtext in [3,4]:
            pygame.mouse.set_visible(False)
            if brienne.textGetDone():
                curtext = 5
                listOBJ.remove(narText.getTextOBJ())
            else:
                brienne.speak(volume)

        elif curtext == 5:
            stacyT = karole.getX() <= stacy.getX() + 130 and karole.getY() + 30 >= stacy.getY()

        elif curtext == 6:
            if stacy.textGetDone():
                curtext = choice("I’m not afraid of her or you!", "Please put me down.", 6, (50, 60), (50, 150))
                if curtext in [7,8]:
                    stacy.createmessage("You’re so funny. I’m going to feel bad for you when Brenda-Simone sticks you on hot lunch duty for the next 6 months. I think you would look cute in a hairnet though, so I’m sure you’ll be able to make it work. You ready to do this hotshot?")
            else:
                stacy.speak(volume)

        elif curtext in [7,8]:
            pygame.mouse.set_visible(False)
            if stacy.textGetDone():
                curtext = 9
                narText.newMessage("Initiate fight with Stacy?")
            else:
                stacy.speak(volume)

        elif curtext == 9:
            if narText.getDone():
                curtext = choice('YES', 'NO', 9, (300, 50), (1000, 50))
                if curtext == 10:
                    stacy.createmessage("Come on hotshot. I know you have it in you. You gonna let Brenda-Simone scare you just as easy too?")
                    curtext = 7
                if curtext == 11:
                    stacyFight()
            else:
                narText.print_lines(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_e:
                    if curtext == 5:
                        if stacyT:
                            listOBJ.append(narText.getTextOBJ())
                            stacy.createmessage("Oh. It’s you. I was wondering when you would finally get to me before Brenda-Simone gets back. What? Don’t look so surprised. You can’t fight everyone and not expect me to eventually guess what your game plan is here. Did you honestly think you were being clever? Well, anyways its too late now. If you can even get past me, Brenda-Simone will put you down quick.")
                            curtext = 6
                            stacyT = False
        pygame.display.update()
        clock.tick(60)



def after_debbie():
    global clock, DISPLAYSURF, karole, debbie, brienne, volume

    hoverO1 = False
    hoverO2 = False
    DISPLAYSURF.fill((255, 255, 255))
    background = Sprite(0, 0, "PTA_meeting_background-1.png.png", 1400, 750, DISPLAYSURF)
    karole.updatePos((600, 400))
    karole.setImg('Karole_walk1.png')
    debbie.updatePos((1200, 400))
    debbie.setImg('Debbie_stationary.png')
    brienne.setImg('brieanne-teigh_simple_sprite copy.png')
    curtext = 0
    karole.createText()
    debbie.createText()
    brienne.createText()
    debbie.createmessage("Geez, I guess I underestimated you Karole. That fight sure was something. Most people can’t get past me, so you may actually have a chance at becoming PTA president.")
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 0)
    narText.newMessage("a")
    listOBJ = [debbie, narText.getTextOBJ()]
    pygame.mouse.set_visible(False)
    brienneT = False
    brienne.setAlpha(0)


    while True:
        while True:
            if curtext in [7]:
                background.draw()
            else:
                DISPLAYSURF.set_clip((0, 300, 1400, 750))
                background.draw()
                DISPLAYSURF.set_clip((0, 0, 1400, 750))

            debbie.draw()
            brienne.draw()
            karole.draw()
            karole.check_move(listOBJ)
            karole.returnTouching(listOBJ)

            if curtext == 0:
                if debbie.textGetDone():
                    curtext = 1
                    debbie.createmessage("If you do, can I count on you for a spot by your side? I only listen to Brenda-Simone because she keeps my dumb kid from getting expelled.")
                else:
                    debbie.speak(volume)

            elif curtext == 1:
                if debbie.textGetDone():
                    curtext = choice("No way!", "Sure, I guess. You did put up a good fight.", 1, (50, 60), (50, 150))
                    if curtext == 3:
                        debbie.createmessage("Ok thats fair")
                    elif curtext == 2:
                        debbie.createmessage("Thanks!")
                else:
                    debbie.speak(volume)

            elif curtext in [2,3]:
                pygame.mouse.set_visible(False)
                if debbie.textGetDone():
                    curtext = 4
                    debbie.createmessage("Well, I’ve got better things to do than sit around and wait for Brenda-Simone. The next person you’re going to want to find in the path to president is Brieanne-Teigh, the goody two shoes. You can always find her by the snack table lecturing everyone on how raw veg veganism will change their lives and going to her hot yoga class will add ten years to their lifespan. Good luck not trying to throttle her immediately.")
                    brienneAlpha = 0
                    listOBJ.append(brienne)
                else:
                    debbie.speak(volume)

            elif curtext == 4:
                if debbie.textGetDone():
                    curtext = choice("I’m not sure...", "Let’s do this!", 4, (50, 60), (50, 150))
                    if curtext == 6:
                        debbie.createmessage("I'm sure you'll do fine drama queen, just go talk to her already!")
                    elif curtext == 5:
                        debbie.createmessage("Hell yea! That's the spirit!")
                else:
                    debbie.speak(volume)
                    if brienneAlpha < 255:
                        brienneAlpha += 1
                        brienne.setAlpha(brienneAlpha)

            elif curtext in [5,6]:
                pygame.mouse.set_visible(False)
                if debbie.textGetDone():
                    curtext = 7
                    listOBJ.remove(narText.getTextOBJ())
                else:
                    debbie.speak(volume)

            elif curtext == 7:
                brienneT = karole.getX() <= brienne.getX() + 130 and karole.getY() + 30 >= brienne.getY()

            elif curtext == 8:
                if brienne.textGetDone():
                    curtext = 9
                    karole.createmessage("Um.... No, I’m good. I heard you’re the next person to fight to get to Brenda-Simone though. Can we just get to it?")
                else:
                    brienne.speak(volume)

            elif curtext == 9:
                if karole.textGetDone():
                    curtext = 10
                    brienne.createmessage("Don’t be silly! We don’t need to fight! Have you ever considered horse therapy for your apparent anger issues? I think you could really benefit...")
                else:
                    karole.speak(volume)

            elif curtext == 10:
                if brienne.textGetDone():
                    curtext = 11
                    karole.createmessage("Are you serious right now? Can we please just fight...")
                else:
                    brienne.speak(volume)

            elif curtext == 11:
                if karole.textGetDone():
                    curtext = 12
                    brienne.createmessage("Of course! If that’s what you want! I’ll always be there for a friend in need! Even if it means beating their face in with no mercy!")
                else:
                    karole.speak(volume)

            elif curtext == 12:
                if brienne.textGetDone():
                    curtext = 13
                    narText.newMessage("Initiate fight with Brieanne-Teigh?")
                else:
                    brienne.speak(volume)

            elif curtext == 13:
                if narText.getDone():
                    curtext = choice('YES', 'NO', 13, (300, 50), (1000, 50))
                    if curtext == 14:
                        pygame.mouse.set_visible(False)
                        brienne.createmessage("That’s fine! Can I interest you in a keto friendly donut until you’re ready?")
                        curtext = 12
                    elif curtext == 15:
                        brieanneFight()
                else:
                    narText.print_lines(volume)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_e:
                        if curtext == 7:
                            if brienneT:
                                listOBJ.append(narText.getTextOBJ())
                                brienne.createmessage("Hi there! Do you have a minute to talk about our lord and savior Jesus Christ?")
                                curtext = 8
                                brienneT = False
            pygame.display.update()
            clock.tick(60)


def after_linda():
    global clock, DISPLAYSURF, karole, linda, debbie, volume

    hoverO1 = False
    hoverO2 = False
    DISPLAYSURF.fill((255, 255, 255))
    background = Sprite(0, 0, "PTA_meeting_background-1.png.png", 1400, 750, DISPLAYSURF)
    karole.updatePos((600, 400))
    karole.setImg('Karole_walk1.png')
    linda.updatePos((1200, 400))
    debbie.setImg('Debbie_stationary_Right.png')
    curtext = 0
    karole.createText()
    linda.createText()
    debbie.createText()
    linda.createmessage("Whew! You're one quick learner! Looks like you have what it takes.")
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 0)
    narText.newMessage("a")
    listOBJ = [linda, narText.getTextOBJ()]
    pygame.mouse.set_visible(False)
    debbie.setAlpha(0)
    Etrigger = False
    debTrigger = False


    while True:
        if curtext in [13, 20]:
            background.draw()
        else:
            DISPLAYSURF.set_clip((0, 300, 1400, 750))
            background.draw()
            DISPLAYSURF.set_clip((0, 0, 1400, 750))

        linda.draw()
        debbie.draw()
        karole.draw()
        karole.check_move(listOBJ)
        t = karole.returnTouching(listOBJ)

        if curtext == 0:
            if linda.textGetDone():
                curtext = 1
            else:
                linda.speak(volume)

        elif curtext == 1:
            curtext = choice("Thanks! You're a great teacher!", "No thanks to you! That training was useless.", 1, (50, 60), (50,150))
            if curtext == 3:
                linda.createmessage("Thanks! Now you have a choice, you can train with me some more or move on to fight the first mom of Brenda-Simone's clique.")

            elif curtext == 2:
                linda.createmessage("Useless? Without me you wouldn’t last one minute against Brenda-Simone. Shut up and keep training with me or get out of my sight and pick a fight with another mom in Brenda-Simone’s clique.")

        elif curtext in [2,3]:
            pygame.mouse.set_visible(False)
            if linda.textGetDone():
                curtext = 4
            else:
                linda.speak(volume)

        elif curtext == 4:
            curtext = choice("FIGHT LINDA AGAIN", "MOVE ON", 4, (100, 100), (900, 100))
            if curtext == 6:
                fight_linda()
            elif curtext == 5:
                linda.createmessage("So you feel you’re up for a challenge, huh? Walking in now is the first roadblock to PTA president, Debbie. Debbie is Brenda-Simone’s muscle and the person responsible for the hole in the wall of the principal’s office.")
                debAlpha = 0
                listOBJ.append(debbie)

        elif curtext == 5:
            pygame.mouse.set_visible(False)
            if linda.textGetDone():
                curtext = 7
            else:
                linda.speak(volume)
                if debAlpha < 255:
                    debAlpha += 1
                    debbie.setAlpha(debAlpha)

        elif curtext == 7:
            curtext = choice("I don’t believe you.", "Really?", 7, (100, 100), (900, 100))
            if curtext != 7:
                linda.createmessage("I am not lying. Her kid got suspended for putting \"graffiti\" all over the bathroom walls and Debbie threw her motorcycle helmet at the secretary. She’s no joke, but you’re more than ready to take her on!")

        elif curtext in [8,9]:
            pygame.mouse.set_visible(False)
            if linda.textGetDone():
                curtext = 10
            else:
                linda.speak(volume)

        elif curtext == 10:
            curtext = choice("I’m not sure...", "Let’s do this!", 10, (100, 100), (900, 100))
            if curtext != 10:
                linda.createmessage("You’re going to be great! Start off by initiating an interaction with Debbie. She’s not the best conversationalist but just about anything will get her mad enough to fight and then you’re one step closer to Brenda-Simone.")

        elif curtext in [11,12]:
            pygame.mouse.set_visible(False)
            if linda.textGetDone():
                curtext = 13
                listOBJ.remove(narText.getTextOBJ())
            else:
                linda.speak(volume)
        elif curtext == 13:
            Etrigger = debTrigger = karole.getX() <= debbie.getX() + 130 and karole.getY() + 30 >= debbie.getY()

        elif curtext == 14:
            if debbie.textGetDone():
                curtext = 15
                karole.createmessage("I hear you’re the person I need to go through to get to Brenda-Simone.")
            else:
                debbie.speak(volume)

        elif curtext == 15:
            if karole.textGetDone():
                curtext = 16
                debbie.createmessage("And what about it? I don’t have time to fight every single mom that walks through these doors. Brenda-Simone is getting her nails done right now and I’m in charge of keeping order around here until she gets back. Don’t pick this fight. You won’t like me when I’m angry.")
            else:
                karole.speak(volume)

        elif curtext == 16:
            if debbie.textGetDone():
                curtext = 17
                narText.newMessage("Initiate fight with Debbie?")
            else:
                debbie.speak(volume)

        elif curtext == 17:
            if narText.getDone():
                curtext = choice('YES', 'NO', 17, (300, 50), (1000, 50))

                if curtext == 18:
                    pygame.mouse.set_visible(False)
                    debbie.createmessage("Knew it! It’s not like you would have won anyway. I’ll be here until you come crawling back again, but until then, scram!")
            else:
                narText.print_lines(volume)

        elif curtext == 18:
            if debbie.textGetDone():
                listOBJ.pop(-1)
                curtext = 20
                debTrigger = True
            else:
                debbie.speak(volume)

        elif curtext == 19:
            debbieFight()

        elif curtext == 20:
            debTrigger = karole.getX() <= debbie.getX() + 130 and karole.getY() + 30 >= debbie.getY()
            linTrigger = karole.getX() + 130 >= linda.getX() and karole.getY() + 30 >= linda.getY()

        elif curtext == 21:
            if linda.textGetDone():
                listOBJ.pop(-1)
                curtext = 20
            else:
                linda.speak(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_e:
                    if Etrigger == True:
                        listOBJ.append(narText.getTextOBJ())
                        debbie.createmessage("What do you think you’re looking at? Move along newbie.")
                        curtext = 14
                        Etrigger = False
                    if curtext == 20:
                        if debTrigger:
                            listOBJ.append(narText.getTextOBJ())
                            narText.newMessage("Initiate fight with Debbie?")
                            curtext = 17
                            debTrigger = False
                        elif linTrigger:
                            listOBJ.append(narText.getTextOBJ())

                            #placeholder line
                            linda.createmessage("What are you scared? Go fight her already!!!")
                            curtext = 21
                            linTrigger = False
        pygame.display.update()
        clock.tick(60)

def stacyFight():
    global clock, DISPLAYSURF, karole, stacy, volume

    bImg = Sprite(0,0,'Hills Free (update 3.0).png', 1400, 550, DISPLAYSURF)
    pImg = Sprite(0, 550, 'fightpanel1.png', 1400, 200, DISPLAYSURF)
    hpBar = Sprite(100, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    hpBarL = Sprite(800, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    font = pygame.font.Font(None, 35)
    karole.updatePos((185, 200))
    stacy.updatePos((1030, 200))
    karole.setImg('Karole_walk1.png')
    stacy.setImg('Stacy_stationary.png')
    stacy.setMaxHp(40)
    stacy.setHP(40)
    karole.setMaxHp(40)
    karole.setHP(40)
    fighters = [karole, brienne]
    lines_to_run = ["0101", "1234", 'Do you have a license to act like this?', 'I am a girlboss first and a mother second!', 'Your kid looks like he skateboards in empty parking lots!', 'I’m going to steal your WholeFoods membership card!']
    stacy.createText(450, 0)
    karole.createText(450, 0)
    fight = Fight([karole, stacy], DISPLAYSURF, volume)
    fight.create_lines(lines_to_run)
    mT = False
    hover = False

    karole.setHP(40)
    karole.setAlive(True)
    stacy.setAlive(True)
    karole.setHeals(3)
    stacy.setHeals(1)
    karole.setEnergy(0)
    stacy.setEnergy(0)

    while True:
        fight.updateFighters([karole,stacy])

        if fight.getFightToggle():

            bImg.draw()
            pImg.draw()
            hpBar.draw()
            hpBarL.draw()
            stacy.draw()
            fight.drawChars()
            kHp = font.render(f'Karole HP: {karole.getHp()}', True, (255, 0, 0))
            dHp = font.render(f'Stacy HP: {stacy.getHp()}', True, (255, 0, 0))
            DISPLAYSURF.blit(kHp, (130, 575))
            DISPLAYSURF.blit(dHp, (1135, 573))
        result = fight.check_fight(volume)
        if result:
            if mT == False:
                #placeholder
                karole.createmessage("Brenda-Simone, here I come! Stacy, you didn’t stand a chance with that off the rack blazer!")
                mT = True
            else:
                if karole.textGetDone():
                    after_stacy()
                else:
                    karole.speak(volume)

        elif result == False:
            if mT == False:
                stacy.createmessage("I can’t help destroying you, Karole. But at least I looked this great while I did it...you’re welcome!")
                mT = True
            else:
                if stacy.textGetDone():
                    game_over()
                    karole.setHP(30)
                    stacyFight()

                else:
                    stacy.speak(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)

def brendaFight():
    global clock, DISPLAYSURF, karole, brenda, volume

    bImg = Sprite(0,0,'Hills Free (update 3.0).png', 1400, 550, DISPLAYSURF)
    pImg = Sprite(0, 550, 'fightpanel1.png', 1400, 200, DISPLAYSURF)
    hpBar = Sprite(100, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    hpBarL = Sprite(800, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    font = pygame.font.Font(None, 35)
    karole.updatePos((185, 200))
    brenda.updatePos((1030, 200))
    karole.setImg('Karole_walk1.png')
    brenda.setImg('Brenda_stationary.png')
    brenda.setMaxHp(40)
    brenda.setHP(40)
    karole.setMaxHp(30)
    karole.setHP(30)
    fighters = [karole, brenda]
    lines_to_run = ["1010", "1234", 'You have just lost a valued customer of this establishment!', 'This is private property!', 'You wouldn’t like me before my coffee!', 'My kids are proudly unvaccinated!']
    brenda.createText(450, 0)
    karole.createText(450, 0)
    fight = Fight([karole, brenda], DISPLAYSURF, volume)
    fight.create_lines(lines_to_run)
    mT = False
    hover = False

    karole.setHP(30)
    karole.setAlive(True)
    brenda.setAlive(True)
    karole.setHeals(3)
    brenda.setHeals(1)
    karole.setEnergy(0)
    brenda.setEnergy(0)

    while True:
        fight.updateFighters([karole,brenda])

        if fight.getFightToggle():

            bImg.draw()
            pImg.draw()
            hpBar.draw()
            hpBarL.draw()
            brenda.draw()
            fight.drawChars()
            kHp = font.render(f'Karole HP: {karole.getHp()}', True, (255, 0, 0))
            dHp = font.render(f'Brenda-Simone HP: {brenda.getHp()}', True, (255, 0, 0))
            DISPLAYSURF.blit(kHp, (130, 575))
            DISPLAYSURF.blit(dHp, (1020, 575))
        result = fight.check_fight(volume)
        if result:
            if mT == False:
                #placeholder
                karole.createmessage("Finally! The ultimate reward! Bow down before your new PTA president! Get lost, Brenda-Simone. I’m ready to take my throne.")
                mT = True
            else:
                if karole.textGetDone():
                    after_brenda()
                else:
                    karole.speak(volume)

        elif result == False:
            if mT == False:
                brenda.createmessage("Just as I expected! There’s no way you could have ever beaten me! No wonder your kid has to sit at the nut allergy table all alone… Get back to the kitchen, Karole. We all know its where you really belong.")
                mT = True
            else:
                if brenda.textGetDone():
                    game_over()
                    karole.setHP(30)
                    brendaFight()
                else:
                    brenda.speak(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)

def brieanneFight():
    global clock, DISPLAYSURF, karole, brienne, volume

    bImg = Sprite(0,0,'Hills Free (update 3.0).png', 1400, 550, DISPLAYSURF)
    pImg = Sprite(0, 550, 'fightpanel1.png', 1400, 200, DISPLAYSURF)
    hpBar = Sprite(100, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    hpBarL = Sprite(800, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    font = pygame.font.Font(None, 35)
    karole.updatePos((185, 200))
    brienne.updatePos((1030, 200))
    karole.setImg('Karole_walk1.png')
    brienne.setImg('Brieanne-Teigh_stationary.png')
    brienne.setMaxHp(40)
    brienne.setHP(40)
    karole.setMaxHp(40)
    karole.setHP(40)
    fighters = [karole, brienne]
    lines_to_run = ["1001", "1234", 'Paleo isn’t a diet, it’s a lifestyle!', 'Soaps made with preservatives are inherently better!', 'Wearing matching pajamas with your family is weird and tacky!', 'You\'re not being very live, laugh, love right now!']
    brienne.createText(450, 0)
    karole.createText(450, 0)
    fight = Fight([karole, brienne], DISPLAYSURF, volume)
    fight.create_lines(lines_to_run)
    mT = False
    hover = False

    karole.setHP(40)
    karole.setAlive(True)
    brienne.setAlive(True)
    karole.setHeals(3)
    brienne.setHeals(1)
    karole.setEnergy(0)
    brienne.setEnergy(0)

    while True:
        fight.updateFighters([karole,brienne])

        if fight.getFightToggle():

            bImg.draw()
            pImg.draw()
            hpBar.draw()
            hpBarL.draw()
            brienne.draw()
            fight.drawChars()
            kHp = font.render(f'Karole HP: {karole.getHp()}', True, (255, 0, 0))
            dHp = font.render(f'Brieanne-Teigh HP: {brienne.getHp()}', True, (255, 0, 0))
            DISPLAYSURF.blit(kHp, (130, 575))
            DISPLAYSURF.blit(dHp, (1020, 575))
        result = fight.check_fight(volume)
        if result:
            if mT == False:
                #placeholder
                karole.createmessage("One step closer to Brenda-Simone! Sorry, but I’m not eating those stupid gluten free cupcakes any more!")
                mT = True
            else:
                if karole.textGetDone():
                    after_brieanne()
                else:
                    karole.speak(volume)

        elif result == False:
            if mT == False:
                brienne.createmessage("One can accomplish anything with the right mindset and diet! Like just absolutely wrecking you the way I just did!  Have you drank water today?")
                mT = True
            else:
                if brienne.textGetDone():
                    game_over()
                    karole.setHP(30)
                    brieanneFight()
                else:
                    brienne.speak(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)

def debbieFight():
    global clock, DISPLAYSURF, karole, debbie, volume

    bImg = Sprite(0,0,'Hills Free (update 3.0).png', 1400, 550, DISPLAYSURF)
    pImg = Sprite(0, 550, 'fightpanel1.png', 1400, 200, DISPLAYSURF)
    hpBar = Sprite(100, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    hpBarL = Sprite(800, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    font = pygame.font.Font(None, 35)
    karole.updatePos((185, 200))
    debbie.updatePos((1030, 200))
    karole.setImg('Karole_walk1.png')
    debbie.setImg('Debbie_stationary.png')
    debbie.setMaxHp(40)
    debbie.setHP(40)
    karole.setMaxHp(40)
    fighters = [karole, debbie]
    lines_to_run = ["01010", "1234567", 'I know your leather jacket is fake! Pleather is so last season!', 'I will key your car after this!', 'Everybody says your kitchen island looks cheap!', 'I bet you still drink soy milk!', 'Even my essential oils can’t cure your attitude!']
    debbie.createText(450, 0)
    karole.createText(450, 0)
    fight = Fight([karole, debbie], DISPLAYSURF, volume)
    fight.create_lines(lines_to_run)
    mT = False
    hover = False

    karole.setHP(40)
    karole.setAlive(True)
    debbie.setAlive(True)
    karole.setHeals(3)
    debbie.setHeals(1)
    karole.setEnergy(0)
    debbie.setEnergy(0)

    while True:
        fight.updateFighters([karole,debbie])

        if fight.getFightToggle():

            bImg.draw()
            pImg.draw()
            hpBar.draw()
            hpBarL.draw()
            debbie.draw()
            fight.drawChars()
            kHp = font.render(f'Karole HP: {karole.getHp()}', True, (255, 0, 0))
            dHp = font.render(f'Debbie HP: {debbie.getHp()}', True, (255, 0, 0))
            DISPLAYSURF.blit(kHp, (130, 575))
            DISPLAYSURF.blit(dHp, (1120, 575))
        result = fight.check_fight(volume)
        if result:
            if mT == False:
                #placeholder
                karole.createmessage("Get out of here biker chick wannabe! There’s no room for you in my vision of the PTA!")

                mT = True
            else:
                if karole.textGetDone():
                    after_debbie()
                else:
                    karole.speak(volume)

        elif result == False:
            if mT == False:
                debbie.createmessage("Take those scraggly split ends and get out of here! We all knew you couldn’t so this.")
                mT = True
            else:
                if debbie.textGetDone():
                    game_over()
                    karole.setHP(30)
                    debbieFight()
                else:
                    debbie.speak(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def fight_linda():
    global clock, DISPLAYSURF, karole, linda, volume

    bImg = Sprite(0,0,'Hills Free (update 3.0).png', 1400, 550, DISPLAYSURF)
    pImg = Sprite(0,550,'fightpanel1.png', 1400, 200, DISPLAYSURF)
    hpBar = Sprite(100, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    hpBarL = Sprite(800, 599, 'hpbar.png', 500, 41, DISPLAYSURF)
    font = pygame.font.Font(None, 35)
    karole.setImg('Karole_walk1.png')
    karole.updatePos((185, 200))
    linda.updatePos((1030, 200))
    linda.setMaxHp(40)
    linda.setHP(40)
    fighters = [karole, linda]
    lines_to_run = ["0101001", '1234567', 'Your kid is never going to make varsity mathletes if he acts like you!', 'I’m uninviting you from brunch!', 'I’m going to get the manager!', 'Your highlights are streaky and I can see gray roots!', 'Those earrings make you look trashy!', 'I can see your chipped nails!', 'Good luck next time sweetie!']
    linda.createText(450, 0)

    karole.setHP(30)
    karole.setAlive(True)
    linda.setAlive(True)
    karole.setHeals(3)
    linda.setHeals(1)
    karole.setEnergy(0)
    linda.setEnergy(0)

    karole.createText(450, 0)
    fight = Fight([karole, linda], DISPLAYSURF, volume)
    fight.create_lines(lines_to_run)
    mT= False
    hover = False

    while True:
        fight.updateFighters([karole,linda])

        if fight.getFightToggle():
            # draws the screen at moment
            bImg.draw()
            pImg.draw()
            hpBar.draw()
            hpBarL.draw()
            linda.draw()
            fight.drawChars()
            kHp = font.render(f'Karole HP: {karole.getHp()}', True, (255, 0, 0))
            lHp = font.render(f'Linda HP: {linda.getHp()}', True, (255, 0, 0))
            DISPLAYSURF.blit(kHp, (130, 575))
            DISPLAYSURF.blit(lHp, (1120, 575))

        result = fight.check_fight(volume)
        if result:
            if mT == False:
                karole.createmessage("Say goodbye to the PTA expenses card! A new president just got in town!")

                mT = True
            else:
                if karole.textGetDone():
                    after_linda()
                else:
                    karole.speak(volume)
        elif result == False:
            if mT == False:
                linda.createmessage("Go ahead and crawl back to your soccer mom van, sweetie. I’m the champ here.")
                mT = True
            else:
                if linda.textGetDone():
                    game_over()
                    karole.setHP(30)
                    fight_linda()
                else:
                    linda.speak(volume)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def choice(l1, l2, curtext, pos1, pos2, fontsize = 70, x=0, y=0):
    global clock, DISPLAYSURF, karole, linda, hover1, hover2, volume

    hover_sound = pygame.mixer.Sound("hoverbutton.mp3")
    click_sound = pygame.mixer.Sound("clickbutton.mp3")
    pygame.mixer.Sound.set_volume(hover_sound, volume)
    pygame.mixer.Sound.set_volume(click_sound, volume)
    narText = Text((255, 255, 255), DISPLAYSURF, y, x)
    font = pygame.font.Font(None, 70)
    noHighlight1 = font.render(l1, True, (255, 255, 255))
    yesHighlight1 = font.render(l1, True, (255, 255, 0))
    noHighlight2 = font.render(l2, True, (255, 255, 255))
    yesHighlight2 = font.render(l2, True, (255, 255, 0))

    pygame.mouse.set_visible(True)
    narText.text_box()
    if noHighlight1.get_rect(x=pos1[0], y=pos1[1]).collidepoint(pygame.mouse.get_pos()):
        if hover1 == False:
            pygame.mixer.Sound.play(hover_sound)
        hover1 = True
        DISPLAYSURF.blit(yesHighlight1, pos1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mixer.Sound.play(click_sound)
                return curtext + 2
    else:
        DISPLAYSURF.blit(noHighlight1, pos1)
        hover1 = False

    if noHighlight2.get_rect(x=pos2[0], y=pos2[1]).collidepoint(pygame.mouse.get_pos()):
        DISPLAYSURF.blit(yesHighlight2, pos2)
        if hover2 == False:
            pygame.mixer.Sound.play(hover_sound)
        hover2 = True
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mixer.Sound.play(click_sound)
                return curtext + 1
    else:
        DISPLAYSURF.blit(noHighlight2, pos2)
        hover2 = False
    return curtext

#whatever happens after home screen
def next_screen():
    global clock, DISPLAYSURF, karole, linda, volume

    hover1 = False
    hover2 = False
    DISPLAYSURF.fill((255, 255, 255))
    background = Sprite(0,0,"PTA_meeting_background-1.png.png", 1400, 750, DISPLAYSURF)
    karole.updatePos((100, 350))
    karole.setImg('Karole_walk1.png')
    linda.updatePos((1200,400))
    narText = Text((255, 255, 255), DISPLAYSURF, 0, 0)
    narText.newMessage("Use WASD to move around the meeting room and interact with other mothers.")
    curtext = 0
    karole.createText()
    linda.createText()
    listOBJ = [linda, narText.getTextOBJ()]
    tutEtrigger = True
    font = pygame.font.Font(None, 70)

    pygame.mouse.set_visible(False)
    hover_sound = pygame.mixer.Sound("hoverbutton.mp3")
    click_sound = pygame.mixer.Sound("clickbutton.mp3")
    pygame.mixer.Sound.set_volume(hover_sound, volume)
    pygame.mixer.Sound.set_volume(click_sound, volume)

    while True:
        if curtext in [2,4]:
            background.draw()
        else:
            DISPLAYSURF.set_clip((0, 300, 1400, 750))
            background.draw()
            DISPLAYSURF.set_clip((0, 0, 1400, 750))
        linda.draw()
        karole.draw()
        karole.check_move(listOBJ)
        t = karole.returnTouching(listOBJ)

        if curtext == 0:
            if narText.getDone() == True:
                curtext = 1
                karole.createmessage("Maybe I should go talk to Linda, by the chairs. I've got a word or two to say to her...")
            else:
                narText.print_lines(volume)
        elif curtext == 1:
            if karole.textGetDone():
                curtext = 2
                listOBJ.remove(narText.getTextOBJ())
            else:
                karole.speak(volume)
        elif curtext == 2:
            if karole.getX() + 130 >= linda.getX() and karole.getY() + 30 >= linda.getY():
                narText.newMessage("Press E to interact with other moms")
                curtext = 3
                listOBJ.append(narText.getTextOBJ())
        elif curtext == 3:
            if narText.getDone():
                curtext = 4
                listOBJ.remove(narText.getTextOBJ())
                tutEtrigger = False
            else:
                narText.print_lines(volume)

        elif curtext == 5:
            if linda.textGetDone():
                curtext = 6
                linda.createmessage("So you’re Brenda-Simone’s newest casualty huh? Well, you’ll fit right in with us over here in the corner.=I’m the oldtimer of this PTA, and back in the day I was president before Brenda-Simone came along.=Of course, I was removed and banned permanently from the position for embezzling money from the budget back in ‘08...but the new rims on my Jeep were totally worth it!=Ah, good times.=You seem a little tense. Brenda-Simone getting under your skin? Boy do I have dirt on her…=That is... if you’re interested? Most of these other moms are too scared to step even a toe out of line. But I think you’ve got what it takes to learn the nitty gritty details about our esteemed leader.=You seem like the type that’s finally ready to take a stand against her, and I can help you with that. What do you say?")
            else:
                linda.speak(volume)

        elif curtext == 6:
            if linda.textGetDone():
                curtext = 7
                narText.newMessage("Accept Linda’s offer of information on how to defeat Brenda Simone?")
            else:
                linda.speak(volume)

        elif curtext == 7:
            curtext = choice('YES', 'NO', 7, (300,50), (1000,50))
            if curtext == 8:
                linda.createmessage("Uh... you sure about that hun? I guess I'll just wait here then...")

        elif curtext == 8:
            pygame.mouse.set_visible(False)
            if linda.textGetDone():
                curtext = 7
            else:
                linda.speak(volume)

        elif curtext == 9:
            fight_linda()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_volume(event)
                if event.key == K_e:
                    if tutEtrigger == False:
                        listOBJ.append(narText.getTextOBJ())
                        linda.createmessage("Hey there! I’m Linda!")
                        curtext = 5

        pygame.display.update()
        clock.tick(60)

def introduction():
    global clock, DISPLAYSURF, karole, brenda, volume
    DISPLAYSURF.fill((0, 0, 0))
    pygame.mouse.set_visible(False)

    messageW = Text((255, 255, 255), DISPLAYSURF, 0, 450, fontsize=40)
    messageR = Text((255, 0, 0), DISPLAYSURF, 0, 450, fontsize=40)
    lines = ["This is Karole.", "Karole is a pillar of her community who has recently moved to suburbia.",
             "She wants nothing more than to be the president of her mediocre son’s school PTA.",
             "The current head of the PTA, Brenda-Simone, hates Karole for spilling organic soy milk on her at the Back to School meeting last month.",
             "Since then, Karole has been shoved to the sidelines, stuck doing Brenda-Simone’s bidding with all the other reject moms, setting up folding chairs and handing out mini donuts.",
             "But Karole is better than this! She refuses to let Brenda-Simone ruin her! She will become PTA president, no matter how many keyed minivans or manicured brawls it takes!",
             "First, why don’t you talk to some of these loser mothers and get some juicy information on Brenda Simone.",
             "I'm sure she has to have some secret weakness hidden away..."]
    curMessage = messageW
    currentText = 0
    messageW.newMessage(lines[0])
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 0, 1400, 450))
    karole.updatePos((650, 175))
    karole.draw()

    while True:
        #animates the intro and reads it to screen using the text class
        if curMessage.getDone() == True:
            if len(lines) > currentText + 1:
                currentText += 1
                if currentText in [0,1,2,5,6]:
                    curMessage = messageW
                else:
                    curMessage = messageR
                if currentText in [0, 1, 2, 5, 6, 7]:
                    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 0, 1400, 450))
                    karole.updatePos((650, 175))
                    karole.draw()
                elif currentText == 3:
                    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 0, 1400, 450))
                    brenda.updatePos((650, 175))
                    brenda.draw()
                elif currentText == 4:
                    pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (0, 0, 1400, 450))
                    brenda.updatePos((500, 175))
                    brenda.updatePos((800, 175))
                    karole.draw()
                    brenda.draw()
                curMessage.newMessage(lines[currentText])
                curMessage.print_lines(volume)
            else:
                next_screen()
        else:
            curMessage.print_lines(volume)
        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(60)

# home screen
def home_screen():
    global clock, DISPLAYSURF

    hover = False
    frames = 0
    curImage = 0
    KlassicKarole = Sprite(0, 0, "title_screen_animation1.jpg", 1400, 600, DISPLAYSURF)
    while True:
        frames += 1
        if frames == 10:
            frames = 0
            curImage += 1
            if curImage == 18:
                curImage = 1
            imageName = "title_screen_animation{}.jpg".format(curImage)
            KlassicKarole.setImg(imageName)
        KlassicKarole.draw()

        #shows the game button, returns true if hover sound has played
        hover = button(DISPLAYSURF, hover)

        for event in pygame.event.get():
            check_volume(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(30)

# the start button
def button(screen, b):
    global volume

    hover_sound = pygame.mixer.Sound("hoverbutton.mp3")
    pygame.mixer.Sound.set_volume(hover_sound, volume)
    click_sound = pygame.mixer.Sound("clickbutton.mp3")
    pygame.mixer.Sound.set_volume(click_sound, volume)

    # position of mouse
    pos = pygame.mouse.get_pos()
    gameButton = Sprite(575,550,"START-deSat.png",200,100, DISPLAYSURF)

    # if the mouse is touching the button
    if gameButton.getRect().collidepoint(pos):
        gameButton.setImg("START-deSat.png")
        # if clicked return True
        if not b:
            pygame.mixer.Sound.play(hover_sound)
        b = True
        for event in pygame.event.get():
            check_volume(event)
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mixer.Sound.play(click_sound)

                # if clicked call the next screen
                brendaFight()
    else:
        gameButton.setImg("START-SAT.png")
        b = False
    gameButton.draw()

    return b

def check_volume(event):
    global volume

    if ((event.type == pygame.KEYDOWN and event.key == K_MINUS)):
        volume -= 0.3
        pygame.mixer.music.set_volume(volume)
    if ((event.type == pygame.KEYDOWN and event.key == K_EQUALS)):
        volume += 0.3
        pygame.mixer.music.set_volume(volume)
    if volume > 1:
        volume = 1.0
    elif volume < 0:
        volume = 0.0
    pygame.mixer.music.set_volume(volume)

# start of the program initilizes
if __name__ == "__main__":
    # initalizing
    pygame.init()

    pygame.mixer.init()
    title_music = pygame.mixer.music.load("title_music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1) # loops title screen music
    pygame.mixer.music.set_volume(0.5)
    volume = 0.5

    clock = pygame.time.Clock()
    FPS = 30
    DISPLAYSURF = pygame.display.set_mode((1400, 750))
    pygame.display.set_caption('Klassic Karole')
    DISPLAYSURF.fill((255, 255, 255))  # color background
    DISPLAYSURF.set_alpha(255)
    curBI = 0
    karole = Karole(0, 0, 100, 250, 30, 20, 14, 3, DISPLAYSURF)
    linda = Character(1150, 490, "Linda_stationary.png", 100, 250, 20, 20, 10, DISPLAYSURF, (51, 51, 255), ['LindaHEAD.png'], 1, "Linda")
    debbie = Character(100, 300, "Debbie_stationary.png", 100, 250, 20, 20, 13, DISPLAYSURF, (0, 255, 239), ['Debbie_detailed_headshot_transcrop.png'], 1, "Debbie")
    brienne = Character(100, 300, "Brieanne-Teigh_stationary.png", 100, 250, 20, 20, 13, DISPLAYSURF, (255, 182, 193), ['brienneT_pixelated_trans-1.png (1).png'], 1, "Brieanne-Teigh")
    stacy = Character(100, 300, "Stacy_stationary.png", 100, 250, 20, 20, 13, DISPLAYSURF, (147, 112, 219), ['StacyHead.png'], 1, "Stacy")
    brenda = Character(100, 300, "Brenda_stationary.png", 100, 250, 20, 20, 13, DISPLAYSURF, (242, 0, 32), ['Brenda_Head.png'], 1, "Brenda")
    home_screen()
