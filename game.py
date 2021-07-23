# This is game.py , it was made using a very simple game pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# I have installed the pygame.
# I did so by:
# 1) opening the command line interface on my computer,
# 2) cd to the directory that this task is located in,
# 3) I followed the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) I also got help from here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1030
screen_height = 670
screen = pygame.display.set_mode((screen_width,
                                  screen_height))  # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the 3 enemies and a prize image).

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
monster = pygame.image.load("monster.jpg")
lion = pygame.image.load("lion.jpeg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

monster_width = monster.get_width()  # add another enemy called monster and its width
monster_height = monster.get_height()  # add another enemy called monster and its height

lion_height = lion.get_height()  # adding the third enemy which is lion it height and width
lion_width = lion.get_width()    # lion image was taken from google

prize_height = prize.get_height()   # add the prize height and width
prize_width = prize.get_width()

#player_height = player.get_height()   # add the prize height and width
#player_width = player.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and 3 enemies as variables.

enemyXPosition = 50
enemyYPosition = 40

playerXPosition = 100
playerYPosition = 50

monsterXPosition = 80
monsterYPosition = 40

lionXPosition = 60
lionYPosition = 45

prizeXPosition = 30
prizeYPosition = 30

# Make the enemy start off screen and at a random y position.
enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

# Make the monster start off screen and at a random y position
monsterXPosition = screen_width
monsterYPosition = random.randint(0, screen_height - monster_height)

# Make the lion start off screen and a a random y position
lionXPosition = screen_width
lionYPosition = random.randint(0, screen_height - lion_height)

# Make the prize start off screen and a a random y position
prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False.
# Boolean values are True or False values that can be used to test conditions and test states that are binary,
# i.e. either one way or the other.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

#  This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later.

while 1:
    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition,
                         playerYPosition))  # This draws the player image to the screen at the position specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(lion, (lionXPosition, lionYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():
        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemies and a prize:
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    lionBox = pygame.Rect(lion.get_rect())
    lionBox.top = lionYPosition
    lionBox.left = lionXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:
    if playerBox.colliderect(enemyBox):
        # Display losing status to the user:
        print("You lose!")
        # Quite game and exit window:
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(lionBox):
        # Display losing status to the user:
        print("You lose!")
        # Quite game and exit window:
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(monsterBox):
        # Display losing status to the user:
        print("You lose!")
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(prizeBox):
        # Display losing status to the user:
        print("You win!")
        pygame.quit()
        exit(0)


# If the enemy is off the screen the user wins the game:
    if enemyXPosition < 0 - enemy_width:
        # Display wining status to the user:
        print("You win!")
        # Quite game and exit window:
        pygame.quit()
        exit(0)
    elif monsterXPosition < 0 - monster_width:
        # Display wining status to the user:
        print("You win!")
        # Quite game and exit window:
        pygame.quit()
        exit(0)
    elif lionXPosition < 0 - lion_width:
        # Display wining status to the user:
        print("You win!")  # You win a prize
        # Quite game and exit window:
        pygame.quit()
        exit(0)

# Make enemies and a prize approach the player.
    enemyXPosition -= 0.20
    monsterXPosition -= 0.40
    lionXPosition -= 0.55
    prizeXPosition -= 0.65

    # ================The game loop logic ends here. =============

