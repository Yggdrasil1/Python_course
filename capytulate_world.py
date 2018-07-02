# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:44:05 2018
"""

import pyoneer_character
import numpy as np

class World:
    
    def __init__(self,char=default):
        
        if char == default:
            self.character = pyoneer_character.Character("human")
        
        else:
            self.character = char
            
        self.worldsize = 7
        
        
        
    def move(self):
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
                
            if userinput == "s":
                new_x = -1 * (5 + (self.character.level - 1) * 3)
                
            if userinput == "d":
                new_y = 5 + (self.character.level - 1) * 3
                
            if userinput == "a":
                new_y = -1 * (5 + (self.character.level - 1) * 3)
    
                
            self.character.x_position = new_x
            self.character.y_position = new_y
            
        else:
            
            if userinput == "w":
                new_x = 1
                
            if userinput == "s":
                new_x = -1 
                
            if userinput == "d":
                new_y = 1
                
            if userinput == "a":
                new_y = -1 
                
            if np.absolute(self.character.x_position + new_x) > self.worldsize and np.absolute(self.character.y_position) < self.worldsize:
                
                print("There is a wall here, i can't move in this direction")
                
            if np.absolute(self.character.y_position + new_y) > self.worldsize and np.absolute(self.character.y_position) < self.worldsize:
                
                print("There is a wall here, i can't move in this direction")    
             
            self.character.x_position += new_x
            self.character.y_position += new_y
             
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        