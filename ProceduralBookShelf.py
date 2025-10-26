import maya.cmds as cmds
import random
import math


class BookshelfGen:
    def __init__(self):
        self.book_materials = {}
        self.wood_materials = {}
        self.created_materials = False

    # wood colors 
    def materials(self):
        try:
        
            wood_types = ['oak', 'mahogany', 'birch', 'walnut']
            wood_colors = {
                    # wood colors
                    'oak': (0.7, 0.5, 0.3),
                    'mahogany': (0.5, 0.2, 0.1),
                    'birch': (0.4, 0.4, 0.3),
                    'walnut': (0.4, 0.3, 0.2)
                    }

            for wood in wood_types:
                mat_name = f"wood_{wood}"
            if not cmds.objExists(mat_name):
                shader = cmds.shadingNode('blinn', asShader=True,
                                          name=mat_name)
                base_color = wood_colors[wood]
                cmds.setAttr(f'{shader}.color', base_color[0],
                             base_color[1], base_color[2], type='double3')
                cmds.setAttr(f'{shader}.specularColor', 0.3, 0.3, 0.3, type='double3')
                cmds.setAttr(f'{shader}.eccentricity', 0.4)
                cmds.setAttr(f'{shader}.reflectivity', 0.1)
                self.wood_materials[wood] = shader

            self.created_materials = True

        except Exception as e:
            cmds.warning(f"Error creating materials: {str(e)}")

    def gen_bookshelf(self, params):
        try:
            if not self.created_materials:
                 self.created_materials()

            bookself_group = cmds.group(empty=True, name=f"bookshelf_{random.randit(
                                        1000,9999)}")
            # shelf structure
            shelf_structure = self.create_shelf_structure(params)
            if shelf_structure:
                 cmds.parent(shelf_structure, bookself_group)

                 cmds.select(bookself_group)
                 return bookself_group
        
        except Exception as e:
            cmds.warning(f"Error creating materials: {str(e)}")
            return None 


    def create_shelf(self, params):

        try:

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
                                depth=depth, name="shelf_top")[0]
            bottom = cmds.polyCube(width=width, height=0.2,
                                depth=depth, name="shelf_bottom")[0]
            
            cmds.move(0, height - 0.1, 0, top)
            cmds.move(0, 0.1, 0, bottom)

            cmds.parent(top, frame_group)
            cmds.parent(bottom, frame_group)

            # shelves

            shelf_spacing = height / num_shelves
            for i in range(1, num_shelves):
                shelf = cmds.polyCube(width=width - 0.2, height=0.1, 
                                      depth=depth - 0.1, name=f"shelf_{i}")[0]
                shelf_y = i * shelf_spacing
                cmds.parent(shelf, frame_group)

            # wood color 
            wood_type = params.get('wood_type', 'oak')
            if wood_type in self.wood_materials:
                children = cmds.listRelatives(frame_group, children=True, fullPath=True) or []

                for child in children:
                    cmds.select(child, replace=True)
                    cmds.hyperShade(assign=self.wood_materials[wood_type])

            return frame_group
        
        except Exception as e:
            cmds.warning(f"Error creating materials: {str(e)}")
            return None 
                
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
