import pygame

class gameObject:
    class collideableObject:
        def __init__(self, radius: int, to_collide):
            pass # TODO: [IMPORTANT] Finish the collideableObject class.

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