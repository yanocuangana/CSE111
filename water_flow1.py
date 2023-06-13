from pytest import approx
import pytest

def main():
    tower_height = float(input("What is the height of the tower: "))
    tank_height = float(input("What is the height of the walls of the tank that is on top of the tower: "))

def water_column_height(tower_height, tank_height):
    
    h = tower_height + (3 * tank_height / 4)
    
    return h
