import pygame
import os
import sys
import random
import time

hammer_tick = 0
hammer_max_tick = 10
while True:
    time.sleep(1)
    print(hammer_tick)
    if hammer_tick < hammer_max_tick:
        hammer_tick += 1

    else:
        hammer_tick = 0
