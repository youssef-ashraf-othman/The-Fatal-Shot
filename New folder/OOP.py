from GUI import *
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True

    def draw(self, surface):
        if self.visible:
            action = False
            # get mouse position
            pos = pygame.mouse.get_pos()

            # check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # draw button on screen
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action


start_button = Button(325, 200, start_img, 1)
exit_button = Button(725, 200, exit_img, 1)
credits_button = Button(540, 450, credits_img, 0.55)
back_button = Button(100, 500, back_img, 0.6)
replay_button = Button(580, 280, replay_img, 0.3)



class Player():  # became easier of want to add more characters
    def __init__(self, x, y, width, height, step):
        self.x = x
        self.y = y
        self.start_x = x  # for collision
        self.start_y = y  # for collision
        self.width = width
        self.height = height
        self.step = step
        self.left = False
        self.right = False
        self.moves = 0
        self.speed = 10
        self.isJumping = False
        self.standing = True
        self.visible = True
        self.hitbox = (self.x + 20, self.y + 10, self.height - 40,
                       self.width - 20)  # hitbox is a rectangle with start, end, width and height

    def draw(self, screen):  # Display Character
        if self.visible:
            if not self.standing:
                if self.left:
                    screen.blit(move_left[self.moves // 2], (self.x, self.y))
                    self.moves += 1
                    if self.moves == 18:  # we have 9 photos for each direction
                        self.moves = 0

                elif self.right:
                    screen.blit(move_right[self.moves // 2], (self.x, self.y))
                    self.moves += 1
                    if self.moves == 18:  # we have 9 photos for each direction
                        self.moves = 0
            else:
                if self.right:
                    screen.blit(move_right[0], (self.x, self.y))
                else:
                    screen.blit(move_left[0], (self.x, self.y))
                # screen.blit(hero, (self.x, self.y))  # fixed hero look at you!
            self.hitbox = (self.x + 20, self.y + 10, self.width - 40, self.height - 20)
            # pygame.draw.rect(screen, TEAL, self.hitbox, 2) #width = 2 ...  # width = 2 # We no longer need to show it

    def hit(self):
        self.x = self.start_x
        self.y = self.start_y
        self.moves = 0

        pygame.display.update()
        # make small mainloop


class Bullet:  # The bullet is a circle
    def __init__(self, x, y, radius, color, direction, step):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction  # -1 to left and 1 to right
        self.step = step * direction
        self.visible=True

    def draw(self, screen):
        if self.visible:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Enemy:  # enemy1 will move to left and right automatically from (x) to (end)
    def __init__(self, x, y, width, height, end, step, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.right = False
        self.left = False
        self.start = x  # because we will modify the value of (x)
        self.step = step
        self.moves = 0
        self.hitbox = (self.x + 20, self.y + 10, self.height - 40,
                       self.width - 20)  # hitbox is a rectangle with start, end, width and height
        self.health = health
        self.visible = True # status of enemy1

    def draw(self, screen):
        if self.visible:
            self.move()

            if self.step < 0:
                screen.blit(move_leftE[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 11 * 2 or self.moves== 10*2:  # we have 11 photos for each direction
                    self.moves = 0

            else:
                screen.blit(move_rightE[self.moves // 2], (self.x, self.y))
                self.moves += 1
                if self.moves == 11 * 2 or self.moves==10*2:  # we have 11 photos for each direction
                    self.moves = 0

            # ractangle above the enemy1 represented as health bar
            pygame.draw.rect(screen, GREEN,
                             (self.hitbox[0] - (enemy1.health * 2.25), self.hitbox[1] - 17, self.health * 6, 15))

    def move(self):  # The same as hero
        if self.step > 0:
            if self.x + self.step > self.end:  # Would be outside the screen if moved to right?
                self.step *= -1  # if true change the direction
            else:
                self.x += self.step
        else:
            if self.x - self.step < self.start:  # Would be outside the screen if moved to left?
                self.step *= -1
            else:
                self.x += self.step
        self.hitbox = (self.x + 20, self.y + 10, self.width - 40, self.height - 20)

        # pygame.draw.rect(screen, GREEN, self.hitbox, 2)  # width = 2 # We no longer need to show it

    def hit(self):
        hitSound.play()
        self.health -= 1
        if self.health == 0:
            self.visible = False
            self.hitbox = (0, 0, 0, 0)


man = Player(1200, 484, 64, 64, 6)
enemy1 = Enemy(10, 484, 64, 64, 1210, 3, 5)