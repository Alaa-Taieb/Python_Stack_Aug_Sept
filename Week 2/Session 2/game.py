# Define a base character class
class Character:
    # Constructor
    def __init__(self, name, attack_power):
        # Instance Attributes
        self.name = name
        self.hp = 100
        self.attack_power = attack_power

    # Instance Method: check if player is alive.
    def is_alive(self):
        return self.hp > 0
    
    # Instance Method: Attack other players
    def attack(self, target):
        if self.is_alive():
            damage = self.attack_power
            actual_damage = target.take_damage(damage)
            print(f"{self.name} attacked {target.name} for {actual_damage} damage!")
        return self
    
    # Instance Method: Take damage.
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} now has {self.hp} HP left.")
        return damage


# A Mage can cast a spell to deal extra damage
class Mage(Character):
    # Constructor
    def __init__(self, name, attack_power, spell_power):
        # Using the parent's constructor to initialize 'name' and 'attack_power'.
        super().__init__(name, attack_power)
        # Initializing 'spell_power' which is unique to the Mage class.
        self.spell_power = spell_power

    # Instance Method: Steal HP from target.
    def cast_spell(self, target):
        if self.is_alive():
            damage = self.spell_power
            extra_hp = target.take_damage(damage)
            self.hp += extra_hp
            print(f"{self.name} cast a spell on {target.name} stealing {extra_hp} HP points!")
        return self

# A Warrior can defend to reduce incoming damage on the next turn.
class Warrior(Character):
    # Constructor
    def __init__(self, name, attack_power, defend_power):
        # Using the parent's constructor to initialize 'name' and 'attack_power'.
        super().__init__(name, attack_power)
        # Initializing 'defend_power' and 'is_defending' which are unique to the Warrior class.
        self.defend_power = defend_power
        self.is_defending = False

    # Instance Method: Prepare for next turn
    def defend(self):
        if self.is_alive():
            self.is_defending = True
            print(f"{self.name} is preparing to defend!")

    # Instance Method: Overriding the parent 'take_damage' method to reduce the damage when the Warrior is defending!
    def take_damage(self, damage):
        if self.is_defending:
            damage -= self.defend_power
            if damage < 0:
                damage = 0
            self.is_defending = False
        super().take_damage(damage)
        return damage
    

def play_turn(player1, player2):
    print("-"*50)
    print(f"{player1.name}'s turn:")
    choice = input(f"Do you want to (A) Attack or use (S) special move? ").lower() # => 'A' => 'a'
    if choice == 's' and isinstance(player1 , Mage):
        player1.cast_spell(player2)
    elif choice == 's' and isinstance(player1, Warrior):
        player1.defend()
    else:
        player1.attack(player2)

    print("*"*50)
    print(f"{player1.name}: {player1.hp} HP!")
    print(f"{player2.name}: {player2.hp} HP!")

def main_game():
    player1 = Mage("Mage Mike", 20, 10)
    player2 = Warrior("Warrior Wendy", 25, 8)

    while player1.is_alive() and player2.is_alive():
        play_turn(player1 , player2)
        if player2.is_alive():
            play_turn(player2 , player1)

    print("---- Game Over ----")
    print(f"{player1.name} | is_alive = {player1.is_alive()}")
    print(f"{player2.name} | is_alive = {player2.is_alive()}")

main_game()