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
            