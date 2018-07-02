# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:44:05 2018
"""

import capytulate_character
import numpy as np

class World:
    
    def __init__(self,char="default"):
        
        if char == "default":
            self.character = capytulate_character.Character("human")
        
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
                
        new_x = 0
        new_y = 0
                
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
            
      
            
    def analyze_userinput(self,some_input):
        """
        checks the userinput and let the character behave accordingly
        """
        
        if some_input in ['move','mv','walk']:
            self.move()
            
        else:
            print("Sorry, i don't understand.")
             
             
    def encounter(self):
        """
        checks the position of the character and faces him with a random 
        encounter if he is not on his safespot (0,0)
        """
        
        x_pos = self.character.x_position
        y_pos = self.character.y_position
        
        if x_pos == 0 and y_pos == 0:
            print("Ah, back in Town, you are in your safespot!")
        elif np.absolute(x_pos) == self.worldsize and np.absolute(y_pos) == self.worlsize:
            print("Bossfight!!")
        
                
    def run(self):
        """
        executing all the methods to let the game flow
        """  
        
        exiting = False
        
        while not exiting:
            userinput_game = str(raw_input("What would you like to do?: "))
            
            if userinput_game in ['Exit','exit','logout','Logout','log out','Log out']:
                exiting = True
                print("See you soon!")
            
            else:
                self.analyze_userinput(userinput_game)
                
                
if __name__ == "__main__":
        
        new_game = World()
        new_game.run()
        
                
                
                
                
                
                
                
                
                
                
                
        