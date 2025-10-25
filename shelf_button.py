import maya.cmds as cmds
import os
import sys


def add_button():
    top_shelf = cmds.shelfTabLayout("shelfLayout", query=True, selectTab=True)

    cmds.shelfButton(
        parent=top_shelf,
        annotation="Procedural Bookshelf Generator",
        label= "Bookshelf Gen",
        image1="commandButton.png",
        command="""
import bookshelf_generator_ui
ui = bookshelf_generator_ui.BookshelfGeneratorUI()
ui.show()
        """,
        sourceType="Python"
    )