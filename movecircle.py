import pygame
import sys, time
W, H = 500, 500
S = pygame.display.set_mode((W, H))

WHI = (255,255,255)
R = (255,0,0)

RA = 25
BX = W // 2
BY = H // 2
SPE = 20
C = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and BY>0:
        BY -= SPE
    if keys[pygame.K_DOWN] and BY < H:
        BY +=SPE
    if keys[pygame.K_LEFT] and BX > 0:
        BX -= SPE
    if keys[pygame.K_RIGHT] and BX < W:
        BX += SPE
    S.fill(WHI)
    pygame.draw.circle(S,R,(BX, BY), RA)
    pygame.display.flip()
    C.tick(30)
