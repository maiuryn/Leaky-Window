import pygame
import random
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from hole import Hole
import time

detector = HandDetector(detectionCon=0.8, maxHands=2)

pygame.init()
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Leaky Window")

surface = pygame.Surface((window.get_width(), window.get_height()), pygame.SRCALPHA)



clock = pygame.time.Clock()

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 700)

holes = []
water_level = 0
difficulty = 1
start_timer = time.time()


def game_over():
    font = pygame.font.SysFont("calibri", 70, True)
    text = font.render("Game over!", 1, (255, 0, 0))
    window.blit(text, (window.get_width() / 2 - text.get_width() / 2, window.get_height() / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()
    quit()

def add_hole():
    while len(holes) < 5:
        x = random.randint(0, window.get_width())
        y = random.randint(0, window.get_height() - int(water_level))
        hole = Hole(x, y, difficulty)
        holes.append(hole)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    hands, img = detector.findHands(img)

    window.blit(frame, (0, 0))

    pygame.draw.rect(surface, (0, 0, 255, 125), (0, window.get_height() - water_level, window.get_width(), water_level))
    window.blit(surface, (0, 0))
    total_leak_rate = 0

    add_hole()
    for hole in holes:
        if hole.progress >= 1:
            holes.remove(hole)

        if hole.is_under_water(window, water_level):
            holes.remove(hole)
            add_hole()
        if hole.update_leakage(window, surface, water_level):
            total_leak_rate += hole.leak_rate

        hole.draw_hole(window)

    if hands:
        for hand in hands:
            for i in range(4, 21, 4):
                x = window.get_width() - hand["lmList"][i][0] + 60
                y = hand["lmList"][i][1]
                for hole in holes:
                    if hole.is_inside_hole(x, y):
                        # hole.progress += hole.clock.tick
                        hole.progress += 0.1
                        print(hole.progress)

                    else:
                        hole.clock.tick()


    font = pygame.font.SysFont("calibri", 30, True)
    timed_score = font.render(f"Tick Tock...{int(time.time() - start_timer)}", 1, (255, 0, 0))
    window.blit(timed_score, (950, 20))

    water_level += total_leak_rate
    if water_level >= window.get_height() - 100:
        game_over()
        # water_level = 0
        # holes.clear()

    pygame.display.update()
    clock.tick(30)