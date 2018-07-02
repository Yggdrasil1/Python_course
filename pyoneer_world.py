# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:44:05 2018

@author: biostudent216
"""

import pyoneer_character

class World:
    
    def __init__(self,char=default):
        
        if char == default:
            
            self.character = pyoneer_character.Character("human")
        
    def move(self,mv_input):
        """
        Method to move the character through the world
        """
        
        allowed_userinput = False     
        
        userinput = ""
        
        while not allowed_userinput:
            userinput = str(raw_input('In which direction do you wish to walk? '
                                    +'[w,a,s,d]: '))
        
            if not userinput in ['w','s','a','d']:
                print("Please only type one of the possible keys.")
                allowed_userinput = False
            else:
                allowed_userinput = True
                
        if self.character.x_position == 0 and self.character.y_position == 0:
            
            if userinput == "w":
                new_x = 5 + (self.character.level - 1) * 3