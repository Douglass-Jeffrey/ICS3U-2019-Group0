#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2019
# This file is the "Space Aliens" game
#   for CircuitPython

import ugame
import stage


def game_scene():
    # this function is the game scene

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("./tiles.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # the ship sprite(the 5th image, starting to count at 0) 
    #   will show up at location (80,60)
    ship = stage.Sprite(image_bank_1, 5, 80, 60)
    sprites.append(ship)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order, ship and background behind
    game.layers = [ship] + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()


if __name__ == "__main__":
    game_scene()
