import pygame

# Need to create a game window for manual override to work

def init():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    # Creates a window that is set to 500 by 500 for users to visualize

def keyPress(keyName):
    # If the key is pressed it will return true, otherwise it will return false
    answer = False
    for events in pygame.event.get(): pass
    inputKey = pygame.key.get_pressed()
    selfKey = getattr(pygame, 'K_{}'.format(keyName))
    if inputKey[selfKey]:
        answer = True
    pygame.display.update()
    # The code above is just registaring keystrokes for users to understand what they are commanding the drone to do.
    return answer

def main():
    if keyPress("LEFT"):
        print("LEFT KEY PRESSED")
    if keyPress("RIGHT"):
        print("RIGHT KEY PRESSED")
    # When it runs this main file, it will constantly check if "a" has been pressed by the user
    # If I run this is as the main file then it will do the following:
    # The code below will run only when this program file is being run
if __name__ == '__main__':
    init()
    while True:
        main()
