import pygame, random

class gameObject:
    class collideableObject:
        def __init__(self, radius: int, pos: list):
            self.radius = radius
            self.pos = pos
            self.last_pos = pos

    def check_collision(self, object1: collideableObject, object2: collideableObject):
        distance = [abs(object1.pos[0] - object2.pos[0]), abs(object1.pos[1] - object2.pos[1])]
        if min(distance) > (object1.radius + object2.radius):
            return
        randobj: self.collideableObject = random.random([object1, object2])
        randobj.pos = randobj.last_pos
        

class character:
    def __init__(self, pygame: pygame, start_pos: tuple[int, int], player: bool = False, chase_player: bool = False, collisions: list = []) -> None:
        self.pos = start_pos
        self.player = player
        self.chase_player = chase_player
        self.collisions = collisions

    def update_collisions(self, update_list: list = False):
        if update_list:
            self.collisions = update_list


    def change_pos(self, new_pos: tuple[int, int]):
        self.pos = new_pos