import pygame
import Cube

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)

def draw_bordered_rect(screen, x,y,w,h, color):
    pygame.draw.rect(screen, BLACK, [x,y,w,h])
    pygame.draw.rect(screen, color, [x+4,y+4, w-8, h-8])


def draw_face(screen, cube, faceNum, x, y):
    for i in range(0,9):
        if i < 3:
            draw_bordered_rect(screen, x+(50*i),y, 50, 50, cube.faces[faceNum][i])
        if i >= 3 and i <= 5:
            draw_bordered_rect(screen, x+(50*(i-3)),y + 50*1, 50, 50, cube.faces[faceNum][i])
        if i > 5:
            draw_bordered_rect(screen, x+(50*(i-6)),y + 50*2, 50, 50, cube.faces[faceNum][i])
            


            
    
pygame.init()

size = [800, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rubik's Cube")

cube = Cube.Cube()

cube.move("TU")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            
    screen.fill(WHITE)

    draw_face(screen, cube, 0,50, 250)
    draw_face(screen, cube, 1, 210, 250)
    draw_face(screen, cube, 2, 370, 250)
    draw_face(screen, cube, 3, 530, 250)
    draw_face(screen, cube, 4, 210, 90)
    draw_face(screen, cube, 5, 210, 410)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
