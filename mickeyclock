import pygame
import sys
from datetime import datetime

pygame.init()

W, H = 1000, 800
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Clock")

MB = pygame.image.load("main-clock.png")  
MHL = pygame.image.load("left-hand.png")  
MHR = pygame.image.load("right-hand.png")  

clock = pygame.time.Clock()
running = True

def func(seconds_angle, minutes_angle):
    S.fill((255, 255, 255))

    
    S.blit(MB, (W // 2 - MB.get_width() // 2, H // 2 - MB.get_height() // 2))

    
    hand_left_rotated = pygame.transform.rotate(MHL, seconds_angle)
    hand_right_rotated = pygame.transform.rotate(MHR, minutes_angle)

    S.blit(hand_left_rotated, (W // 2 - hand_left_rotated.get_width() // 2, H // 2 - hand_left_rotated.get_height() // 2))
    S.blit(hand_right_rotated, (W // 2 - hand_right_rotated.get_width() // 2, H // 2 - hand_right_rotated.get_height() // 2))

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    CT = datetime.now().time()
    seconds = CT.second
    minutes = CT.minute

    
    seconds_angle = -seconds * 6  
    minutes_angle = -minutes * 6  

    func(seconds_angle, minutes_angle)

    clock.tick(1)  

pygame.quit()
sys.exit()
