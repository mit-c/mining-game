from SpriteReader import SpriteReader
from MapClasses.CollisionMap import CollisionMap
import pygame as pyg
import init
from InputHandler import InputHandler
from Renderer import Renderer


def main():
    maps = {
        "collision_map": CollisionMap("src\maps\starting_point.txt")
    }
    screen, scene = init.game()
    running = True
    input_handler = InputHandler(scene, maps)
    sprites = SpriteReader()

    renderer = Renderer(screen, scene, maps, sprites)
    while running:

        main_loop(input_handler, scene, renderer, maps)


def main_loop(input_handler, scene, renderer, maps):

    # This checks for quit and changes scene.player_phsyics
    input_handler.get_events()
    scene.player_physics.update_pos(scene)
    renderer.paint()


main()
