# Improvements
# - Resizable window
# - Test hanging issue
#
import pygame,time,sys
from random import randrange

def string_it(screen,color):
    width = screen.get_width()
    height = screen.get_height()
    delay = 0.001
    for i in range(0,width,8):
        pygame.draw.line(screen,color,(0,height-i), (i,0))
        time.sleep(delay)
        pygame.display.flip()
    for i in range(0,width,8):
        pygame.draw.line(screen,color,(i,0), (height,i))
        time.sleep(delay)
        pygame.display.flip()
    for i in range(0,width,8):
        pygame.draw.line(screen,color,(height,0+i), (height-i,height))
        time.sleep(delay)
        pygame.display.flip()
    for i in range(0,width,8):
        pygame.draw.line(screen,color,(0,height-i), (height-i,height))
        time.sleep(delay)
        pygame.display.flip()

def main():
    black = (0,0,0)
    (width, height) = (800, 800)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('String Art')
    screen.fill(black)
    running = True
    while running:
        color = pygame.Color(randrange(256), randrange(256), randrange(256))
        string_it(screen,color)
        string_it(screen,black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("quit.")
    pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
