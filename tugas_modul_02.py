import random

class Robot:
    def __init__(self, name, attack, health, accuracy, comp=False):
        self.name = name
        self.attack = attack
        self.health = health
        self.accuracy = accuracy
        self.defending = False
        self.comp = comp

    def attack_enemy(self, enemy):
        if random.random() <= self.accuracy:
            damage = self.attack // 2 if enemy.defending else self.attack
            enemy.health -= damage
            print(f"------------ {self.name} menyerang {enemy.name} dan memberikan {damage} damage! ------------")
        else:
            print(f"------------ {self.name} gagal menyerang (skill issue) ------------")

    def defend(self):
        self.defending = True
        print(f"{self.name} Bertahan!")

    def health(self):
        return self.health > 0

    def reset_defense(self):
        self.defending = False

    def choose_action(self):
        if self.comp:
            return str(random.choice(["1", "2"]))
        else:
            print("\n1. Attack     2. Defense     3. Giveup")
            return input(f"{self.name}, pilih aksi: ")

class Game:
    def __init__(self, bot1, bot2):
        self.bot1 = bot1
        self.bot2 = bot2

    def start(self):
        round = 1
        while self.bot1.health and self.bot2.health:
            print(f"\n================================= Round-{round} =================================")
            print(f"\n{self.bot1.name} [{self.bot1.health}]")
            print(f"{self.bot2.name} [{self.bot2.health}]")
            print(f"\n=================================  Start  =================================")

            choice1 = self.bot1.choose_action()
            choice2 = self.bot2.choose_action()
            
            if choice1 == "3":
                print(f"\n{self.bot1.name} menyerah! {self.bot2.name} menang!")
                return
            elif choice1 == "2":
                self.bot1.defend()
            elif choice1 == "1":
                self.bot1.attack_enemy(self.bot2)
            
            if choice2 == "3":
                print(f"\n{self.bot2.name} menyerah! {self.bot1.name} menang!")
                return
            elif choice2 == "2":
                self.bot2.defend()
            elif choice2 == "1":
                self.bot2.attack_enemy(self.bot1)
            
            self.bot1.reset_defense()
            self.bot2.reset_defense()
            round += 1
        
        if self.bot1.health:
            print(f"\n{self.bot1.name} menang!")
        else:
            print(f"\n{self.bot2.name} menang!")

def main_menu():
    while True:
        print("\nWelcome Traveler!")
        print("1. Start")
        print("2. Exit")
        choice = input("Pilih menu: ")

        if choice == "1":
            print("\n1. Vs AI")
            print("2. Vs Player")
            mode = input("Pilih mode: ")

            player_name = input("Masukkan nama Anda: ")
            bot1 = Robot(player_name, attack=1, health=10, accuracy=0.8)
            
            if mode == "1":
                bot2 = Robot("Phrolova", attack=1, health=10, accuracy=0.8, comp=True)
            else:
                opponent_name = input("Masukkan nama lawan: ")
                bot2 = Robot(opponent_name, attack=1, health=10, accuracy=0.8)
            
            game = Game(bot1, bot2)
            game.start()
        elif choice == "2":
            print("GGWP!")
            break
        else:
            print("Lhooo nyari apatuch")

if __name__ == "__main__":
    main_menu()
