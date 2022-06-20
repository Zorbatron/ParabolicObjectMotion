from os import system, name
import constants
import sys
import math

def vixviy():
    print("vix and xiy selected")

def vitheta():
    print("vi and angle selected")

def delete_last_lines(n): 
    for _ in range(n): 
        sys.stdout.write(constants.CURSOR_UP_ONE) 
        sys.stdout.write(constants.ERASE_LINE) 

def clear():
    _ = system('cls') if name == 'nt' else system('clear')