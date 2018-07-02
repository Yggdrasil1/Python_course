# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Character:
    
    def __init__(self,race):

        #basic stats        
        self.strength = 5
        self.intelligence = 5
        self.dexterity = 5
        self.luck = 5
        
        #Character coordinates
        self.x_position = 0
        self.y_position = 0
        
        #character class
        self.race = "human"
        
        #character level
        self.level = 1
        
        #fighting stats+
        self.max_hp = self.strength * 4
        self.max_mana = self.intelligence * 3
        
        self.hp = self.max_hp
        self.mana = self.max_mana
        
        
    def move(self,direction):
        
        if direction == "w":
            self.y_position += 1
            
        if direction == "s":
            self.y_position -= 1
            
        if direction == "d":
            self.x_position += 1
            
        if direction == "a":
            self.x_position -= 1
            
    def level_up(self):
        
        if self.race == "human":
            
            self.level += 1
            self.strength += 2
            self.dexterity += 2
            self.intelligence += 2
            self.luck += 1
            
        self.max_hp = self.strength * 4
        self.max_mana = self.intelligence * 3
            
        self.hp = self.max_hp
        self.mana = self.max_mana
        
        