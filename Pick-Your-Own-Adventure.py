import time
import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.mana = 0  # Mana for all classes
        self.max_mana = 0  # Maximum mana for all classes
        self.attack_damage = 10
        self.special_attack_damage = 20
        self.defense = 0
        self.inventory = {
            'health_potions': 3,
            'mana_potions': 3
        }

        # Set stats and special attacks based on class
        if self.player_class == "Warrior":
            self.defense = 10
            self.mana = 20
            self.max_mana = 20
            self.attack1_name = "Sword Slash"
            self.attack2_name = "Shield Bash"
        elif self.player_class == "Mage":
            self.defense = 5
            self.mana = 50
            self.max_mana = 50
            self.attack1_name = "Arcane Bolt"
            self.attack2_name = "Ice Shard"
        elif self.player_class == "Rogue":
            self.defense = 3
            self.mana = 30
            self.max_mana = 30
            self.attack1_name = "Dagger Throw"
            self.attack2_name = "Shadow Strike"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}/{self.max_mana}")
        print("Inventory:", self.inventory)

    def perform_special_attack(self, enemy):
        if self.mana >= 20:
            if self.player_class == "Warrior":
                print(f"{self.name} performs a powerful cleave attack!")
                enemy.health -= self.special_attack_damage
            elif self.player_class == "Mage":
                print(f"{self.name} casts a fireball at {enemy.name}!")
                enemy.health -= self.special_attack_damage
            elif self.player_class == "Rogue":
                print(f"{self.name} executes a deadly backstab on {enemy.name}!")
                enemy.health -= self.special_attack_damage
            self.mana -= 20
        else:
            print("Not enough mana to perform a special attack!")

    def perform_attack1(self, enemy):
        if self.player_class == "Warrior":
            damage = self.attack_damage + 5
            print(f"{self.name} performs a {self.attack1_name}!")
            enemy.health -= damage
        elif self.player_class == "Mage":
            damage = self.attack_damage + 3
            print(f"{self.name} casts {self.attack1_name} at {enemy.name}!")
            enemy.health -= damage
            self.mana -= 5
        elif self.player_class == "Rogue":
            damage = self.attack_damage + 4
            print(f"{self.name} throws a {self.attack1_name} at {enemy.name}!")
            enemy.health -= damage

    def perform_attack2(self, enemy):
        if self.player_class == "Warrior":
            damage = self.attack_damage + 7
            print(f"{self.name} performs a {self.attack2_name}!")
            enemy.health -= damage
        elif self.player_class == "Mage":
            damage = self.attack_damage + 4
            print(f"{self.name} casts {self.attack2_name} at {enemy.name}!")
            enemy.health -= damage
            self.mana -= 8
        elif self.player_class == "Rogue":
            damage = self.attack_damage + 6
            print(f"{self.name} executes a {self.attack2_name} on {enemy.name}!")
            enemy.health -= damage

class Enemy:
    def __init__(self, name, health, attack_damage, defense):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.defense = defense

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(1)
    print("Do you want to enter the cave? (yes/no)")

def choose_class():
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    choice = input("Enter the number of your class: ")
    if choice == "1":
        return "Warrior"
    elif choice == "2":
        return "Mage"
    elif choice == "3":
        return "Rogue"
    else:
        print("Invalid choice. Please try again.")
        return choose_class()

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name} (Health: {player.health}, Mana: {player.mana}/{player.max_mana}) vs "
              f"{enemy.name} (Health: {enemy.health})")
        print("1. Attack")
        print("2. Special Attack")
        print("3. Use Health Potion")
        print("4. Use Mana Potion")
        print("5. Run")
        choice = input("Choose your action: ")
        if choice == "1":
            player.perform_attack1(enemy)
        elif choice == "2":
            player.perform_special_attack(enemy)
        elif choice == "3":
            if player.inventory['health_potions'] > 0:
                player.health = min(100, player.health + 20)
                player.inventory['health_potions'] -= 1
                print(f"{player.name} used a health potion. Health restored to {player.health}.")
            else:
                print("You don't have any health potions left!")
        elif choice == "4":
            if player.inventory['mana_potions'] > 0:
                player.mana = min(player.max_mana, player.mana + 10)
                player.inventory['mana_potions'] -= 1
                print(f"{player.name} used a mana potion. Mana restored to {player.mana}.")
            else:
                print("You don't have any mana potions left!")
        elif choice == "5":
            print("You managed to escape.")
            break
        else:
            print("Invalid choice. Please try again.")

        if enemy.health > 0:
            player.health -= max(0, enemy.attack_damage - player.defense)
            print(f"{enemy.name} hits you for {max(0, enemy.attack_damage - player.defense)} damage!")

    if player.health > 0:
        print(f"\nYou defeated the {enemy.name}!")

def cave(player):
    print("\nYou enter the dark cave.")
    time.sleep(1)
    print("After walking for a while, you encounter a hostile creature.")
    while True:
        enemy = random.choice(enemies)
        battle(player, enemy)
        if player.health <= 0:
            print("You were defeated in battle. Game over.")
            break
        print("\nYou continue deeper into the cave.")
        time.sleep(1)
        print("Suddenly, another creature appears!")
        time.sleep(1)
        next_action = input("Do you want to keep going deeper into the cave? (yes/no): ")
        if next_action.lower() != "yes":
            break
    if player.health > 0:
        print("\nYou emerge from the cave and find yourself in a dense forest.")
        time.sleep(1)
        print("As you explore further, you stumble upon an ancient temple.")
        time.sleep(1)
        print("You enter the temple cautiously, sensing a powerful presence within...")

def battle_boss(player):
    boss = Enemy("Evil Boss", 120, 20, 15)  # Example boss with higher defense
    print("\nYou confront the Evil Boss!")
    time.sleep(1)
    print("This is the final battle, prepare yourself!")
    time.sleep(1)
    battle(player, boss)

def play_game():
    intro()
    choice = input("(yes/no): ").lower()
    if choice == "yes":
        name = input("Enter your name: ")
        player_class = choose_class()
        player = Player(name, player_class)
        player.display_info()
        cave(player)
        if player.health > 0:
            battle_boss(player)
            if player.health > 0:
                print("\nCongratulations! You defeated the Evil Boss and saved the day!")
            else:
                print("\nYou were defeated by the Evil Boss. Better luck next time!")
    elif choice == "no":
        print("\nYou decide not to enter the cave. The end.")
    else:
        print("Invalid choice. Please try again.")
        play_game()

enemies = [
    Enemy("Goblin", 50, 8, 3),
    Enemy("Skeleton", 60, 10, 2),
    Enemy("Orc", 70, 12, 4),
    Enemy("Troll", 90, 15, 6),
    Enemy("Witch", 80, 13, 3)
]

play_game()

