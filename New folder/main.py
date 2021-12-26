import sys
from OOP import *
score = 0
def redrawGame(score,level):  # Display every thing
    global moves

    text1 = font.render("Score = " + str(score), True, OLIVE)  # Change the color
    text2 = font.render("level = " + str(level), True, OLIVE)
    my_font = pygame.font.SysFont('bold', 100)
    text3 = my_font.render('GAME OVER !', False, (225, 0, 0))
    text4 = my_font.render('YOU WON !', False, (0, 0, 225))


    # screen.fill(BLACK)  # Clear the Effect of moving of rectangle
    screen.blit(backgroundImage, (0, 0))  # Background and its position

    screen.blit(text1, (900, 0))  # show scoring
    screen.blit(text2, (100, 0))
    if score < 0:
        screen.blit(text3, (420, 150))
    if level==10:
        screen.blit(text4,(450,150))




    enemy1.draw(screen)  # Display enemy11
    man.draw(screen)  # Display hero
    for bullet in bullets:  # Display many of bullets
        bullet.draw(screen)

    # pygame.draw.rect(screen, RED, (x, y, width, height))  # Draw rectangle in Window at point(x, y) from (0, 0) ... (0, 0) = most of top-left

    pygame.display.update()  # update the window with new additions


bullets = []  # to be able to hit more than one bullet ... it is empty and filled with Bullet object




# game loop
new_step = enemy1.step
back_button.visible = 0
replay_button.visible = 0

run = True
while run:


    if start_button.draw(screen) or replay_button.draw(screen):
        backgroundImage = pygame.image.load("bg.png")
        new_step = 3
        enemy1.health = 5
        man.step = 6
        level=1
        score=0
        man.visible=1
        r=1
        while r==1:  # use while loop to make window stable
            # pygame.time.delay(50)      #after each 50ms, process user input ... The lower you go, the faster the movement speed
            clock.tick(30)  # FBS = 50 rather than delay(50)

            x_mid = (2 * man.hitbox[0] + man.hitbox[2]) // 2
            y_mid = (2 * man.hitbox[1] + man.hitbox[3]) // 2

            if x_mid > enemy1.hitbox[0] and x_mid < enemy1.hitbox[0] + enemy1.hitbox[
                2]:  # hitting ... if bullet inside the hitbox of enemy1 () ... hitbox[2] = width
                if y_mid > enemy1.hitbox[1]:  # Is the bullet under the The enemy1's top line?

                    score -= 10
                    enemy1.x = 0
                    man.hit()

            for event in pygame.event.get():  # this is list get all actions that user did during last 100ms ... user action would be stored in pygame event
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:  # K_DOWN => when u press on some button
                    if event.key == pygame.K_SPACE:  # hit bullets

                        bulletSound.play()

                        direction = 1
                        if man.right:
                            direction = 1
                        else:
                            direction = -1
                        bullets.append(
                            Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, RED, direction,
                                   10))

            keys = pygame.key.get_pressed()  # It's dectionary recive all actions that user did when pressed on buttons to move rectangle

            # Movement Buttons

            for bullet in bullets:
                if bullet.x > enemy1.hitbox[0] and bullet.x < enemy1.hitbox[0] + enemy1.hitbox[
                    2]:  # hitting ... if bullet inside the hitbox of enemy1 () ... hitbox[2] = width
                    if bullet.y > enemy1.hitbox[1]:  # Is the bullet under the The enemy1's top line?
                        bullets.remove(bullet)  # Because bullet hit the enemy1 ... remove = hide it
                        enemy1.hit()
                        score += 1

                if bullet.x < SCREEN_WIDTH and bullet.x > 0:  # inside the screen
                    bullet.x += bullet.step
                else:
                    bullets.remove(bullet)

            # make it in event to shoot one bullet for each pressing on (z)
            # if keys[pygame.K_z]: #hit bullets
            #     if len(bullets) < 5: #make limit of Bullets
            #         direction = 1
            #         if man.left:
            #             direction = -1
            #         else:
            #             direction = 1
            #         bullets.append(Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, RED, direction, 10))

            if (man.x < enemy1.x and enemy1.right == 0):
                enemy1.step = -new_step
            # the enemy follows hero
            if (man.x > enemy1.x and enemy1.left == 0):
                enemy1.step = new_step

            if keys[pygame.K_LEFT] and man.x - man.step >= 0:  # x - step >= 0 until not to move outside the window
                man.x -= man.step
                man.right = False
                man.left = True
                man.standing = False
            elif keys[pygame.K_RIGHT] and man.x + man.step + man.width <= SCREEN_WIDTH:
                man.x += man.step
                man.right = True
                man.left = False
                man.standing = False
            else:
                man.standing = True
                man.moves = 0
            if not man.isJumping:  # During Jumping, he can't move to up or down
                # Don't need vertical movement
                # if keys[pygame.K_UP] and y - step >= 0:
                #     y -= step
                # if keys[pygame.K_DOWN] and y + step + height <= screenHeight:
                #     y += step
                if keys[pygame.K_UP]:
                    man.isJumping = True
            else:  # in case Jumping
                if man.speed >= -10:
                    neg = 1
                    if man.speed < 0:
                        neg = -1
                    man.y -= (man.speed ** 2) * 0.3 * neg
                    man.speed -= 1
                else:
                    man.speed = 10  # reset for next Jump
                    man.isJumping = False

            if enemy1.visible == 0  :  # for leveling up
                for bullet in bullets:
                    bullet.visible=0
                    bullet.x=0
                level += 1
                man.step += 0.75
                enemy1.visible = 1
                enemy1.health = (level / 2) * 10
                enemy1.x = 0
                new_step += 0.5






            if score < 0 or level ==10:
                redrawGame(score,level)
                credits_button.visible = 0
                start_button.visible = 0
                exit_button.visible = 0
                back_button.visible = 1
                replay_button.visible=1
                for bullet in bullets:
                    bullet.visible=0
                r=0

            redrawGame(score,level)

    elif exit_button.draw(screen):
        sys.exit()
    elif credits_button.draw(screen):
        backgroundImage = pygame.image.load("bg4.jpg")
        screen.blit(backgroundImage, (0, 0))
        exit_button.visible = 0
        start_button.visible = 0
        credits_button.visible = 0
        back_button.visible = 1
        screen.blit(textsurface, (400, 0))
        screen.blit(textsurface1, (400, 75))
        screen.blit(textsurface2, (400, 150))
        screen.blit(textsurface3, (400, 225))
        screen.blit(textsurface4, (400, 300))
        screen.blit(textsurface5, (400, 375))
        screen.blit(textsurface6, (400, 450))

    if back_button.draw(screen):
        backgroundImage = pygame.image.load("bg4.jpg")
        screen.blit(backgroundImage, (0, 0))
        screen.blit(main_menu, (450, 20))
        screen.blit(game_name, (480, 200))
        exit_button.visible = 1
        start_button.visible = 1
        credits_button.visible = 1
        back_button.visible = 0
        replay_button.visible=0





    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()

pygame.quit()





