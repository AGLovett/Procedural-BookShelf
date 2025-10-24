import maya.cmds as cmds
import random
import math 
from Pyside import Qtcore 

class BookshelfGen:

    def create_shelf(self, params):
        width = params['width']
        height = params['height']
        depth = params['shelf_depth']
        num_shelves = params['num_shelves']

        # main frame
        frame_group = cmds.group(empty=True, name="shelf_frame")

        left_side = cmds.polyCube(width=.02, height=height, depth=depth,
                                  name="shelf_left_side"[0])
        right_side = cmds.polyCube(width=.02, height=height, depth=depth,
                                  name="shelf_right_side"[0])
        # sides
        left_x = -width/2 + 0.1
        right_x = -width/2 + 0.1
        cmds.move(left_x, height/2, 0, left_side)
        cmds.move(right_x, height/2, 0, right_side)

        cmds.parent(left_side, frame_group)
        cmds.parent(right_side, frame_group)

        # top/bottom
        top = cmds.polyCube(width=width, height=0.2,
                            depth=depth, name= "shelf_top")[0]
        bottom = cmds.polyCube(width=width, height=0.2,
                            depth=depth, name= "shelf_bottom")[0]
        
        cmds.move(0, height - 0.1, 0, top)
        cmds.move(0, 0.1, 0, bottom)

        cmds.parent(top, frame_group)
        cmds.parent(bottom, frame_group)
    
   


# make a group for whole shelf
# make the shelf 
# Add books (books match prams of shelf)
# return


# create_shelf 
# generate the whole shelf
# add wood color 

# add_books 
# calculate the amount of books that can fit
# add books till reaches max amount space
# book prams (random height, width, depth)
# put books next to eachother 
# put color on books randomly 

# create_book
# create book
# add color
