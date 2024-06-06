# ------------ imports ------------
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ------------ setup ------------
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

# ------------ game loop ------------
while True:
    os.system("clear")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
