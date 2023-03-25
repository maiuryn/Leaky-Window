import pygame
import random
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from hole import Hole

detector = HandDetector(detectionCon=0.8, maxHands=2)

pygame.init()
window = pygame.display.set_mode((1200, 700))

clock = pygame.time.Clock()

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 700)

holes = []
water_level = 0

def add_hole():
    if len(holes) < 6:
        x = random.randint(0, window.get_width())
        y = random.randint(0, window.get_height() - water_level)
        hole = Hole(x, y)
        holes.append(hole)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    ret, img = cap.read()
    hands, img = detector.findHands(img)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    window.blit(frame, (0, 0))

    for hole in holes:
        hole.draw_hole(window)
        hole.update_leakage(window)
    add_hole()

    if hands:
        for hand in hands:
            for i in range(4, 21, 4):
                x = hand["lmList"][i][0]
                y = hand["lmList"][i][1]
                # if x, y is within the holes

    pygame.display.update()
    clock.tick(30)