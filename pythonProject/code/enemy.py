#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Speed Background
        if self.rect.right <= 0:  # Move Background
            self.rect.left = WIN_WIDTH  # Move Background
