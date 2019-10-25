
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100



################### Characters and factions ########################


class player:
    def __init__(self):
        self.name = ''
        self.money = 1000
        self.sanity = 0
        self.location = 'home'
mc = player()

class Russian:
    def __init__(self, n, f, p):
        self.name = n
        self.faction = f
        self.personality = p
    
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Russian("Dimitri", "Communist", "Heroic")
r2 = Russian("Linda", "Communist", "honest")

class American:
    def introduce_self(self):
        print("My name is " + self.name)
        
    def __init__(self, n, f, p, s):
        self.name = n
        self.faction = f
        self.personality = p
        self.is_spy = s
        
    def is_spy(self):
        self.is_spy = True
        
    def is_not_spy(self):
        self.is_spy = False


a1 = American("John", "Capitalist", "rude", False)
a2 = American("Gertrude", "Communist", "nice", True)


a2.american_target = a1

################## The title screen and menus #################

def title_screen():
    os.system('cls')
    print('###############')
    print('#   WElCOME   #')
    print('###############')
    print('     -Play-    ')
    print('     -Help-    ')
    print('     -Quit-    ')
    title_screen_selections()

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif  option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("menu"):
        title_screen()
    else:
        print("Please inpput a valid command")
        title_screen_selections()

def help_menu():
    os.system('cls')
    print('###########################')
    print('#   This is a help menu   #')
    print('###########################')
    print('Type menu to return to menu')
    title_screen_selections()

def start_game():
    print('###  The game will start at a later date  ###')

title_screen()
