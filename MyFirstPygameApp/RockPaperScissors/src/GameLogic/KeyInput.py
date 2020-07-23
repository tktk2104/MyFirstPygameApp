import pygame
from pygame.locals import *

class KeyInput:
    def __init__(self):
        self.curInputData = pygame.key.get_pressed()
        self.preInputData = pygame.key.get_pressed()

    def updateKey(self):
        self.preInputData = self.curInputData
        self.curInputData = pygame.key.get_pressed()

    def isPush(self, keyType):
        return self.curInputData[keyType]

    def isTrigger(self, keyType):
        return self.curInputData[keyType] and not self.preInputData[keyType]
