print("Welcome to Tom\'s escape room! \n")
print("You are in a small room, from which you must escape! \nTo your right is the door, which seems to have an electronic lock with a keypad. \nIn front of you is a desk. \nBehind you in the corner is a cupboard. \nOn the wall to your left is a clock, and a shelf with a picture on it.\nThere is a plant in the corner to your right.")

class Player:
    def __init__(self):
        self.inventory = []
        
player = Player()

class Key:
    def __init__(self, name):
        self.name = name

desk_key = Key("desk key")
cupboard_key = Key("cupboard key")
screwdriver = Key("screwdriver")

class Door:
    def __init__(self, code):
        self.code = code
        self.is_locked = True
    def unlock(self):
        self.is_locked = False
        print("Congratulations! The door is unlocked and you have escaped!")
    def input_code(self, attempt):
        if int(attempt) == self.code:
            self.unlock()
        else:
            print("Access Denied")
            self.inspect()
    
    def inspect(self):
        print("The door looks very sturdy. It has an electronic lock with a numeric keypad. There are four underscores on the digital display, so it looks like you'll need a 4-digit code to unlock the door.")
        user_input = input("Would you like to input a code? Type y/n: ")
        if user_input == 'y':
            user_attempt = input("Enter a 4-digit code: ")
            self.input_code(user_attempt)
        elif user_input == 'n':
            main()
    
door = Door(2583)

class Desk:
    def inspect(self):
        print("There is a wooden desk with a framed picture on it. The desk has a drawer with a keyhole.")
        choice = input("Would you like to interact with the desk? Type y/n: ")
        if choice == 'y':
            self.interact()
        elif choice == 'n':
            main()
        else:
            print("Try again")
            self.inspect()
    def interact(self):    
        choice = input("What would you like to interact with? Type \'picture\' or \'drawer\'.")
        if choice == 'picture':
            print("The picture is of an old man smiling for the camera. You turn the picture over and see the number 3 written on the back.")
            self.inspect()
        elif choice == 'drawer':
            if desk_key in player.inventory:
                print("You have unlocked the desk drawer. Inside is a piece of paper with \" L Q E U B S C Y V \" written on it. There is also an old mobile phone. The battery is dead.")
                self.inspect()
            else:
                print("The desk drawer is locked and you do not have the key.")
                self.inspect()
        else:
            print("Try again")
            self.interact()

desk = Desk()

class Plant:
    def inspect(self):
        if cupboard_key not in player.inventory:
            print("You lift the plant pot up.  Underneath is a key. You pick up the key.")
            player.inventory.append(cupboard_key)
            main()
        else:
            print("You have taken the key, and there is nothing else of interest about the plant.")
            main()

plant = Plant()

class Shelf:
    def inspect(self):
        print("There is a single framed picture on the shelf. It is an old faded photo of a young boy. You pick it up and turn it over and you see the number 7 written on the back.")
        main()

shelf = Shelf()

class Clock:
    def inspect(self):
        print("There is a clock hanging on the wall. You pick it up and turn it around.  The mechanism is concealed by a panel affixed with four screws.")
        choice = input("Would you like to interact with the clock? Type y/n: ")
        if choice == 'y':
            if (screwdriver in player.inventory) and (desk_key not in player.inventory):
                print("You unscrew the panel on the back of the clock. Inside is a key. You pick up the key.")
                player.inventory.append(desk_key)
                main()
            elif (screwdriver in player.inventory) and (desk_key in player.inventory):
                print("You have taken the key and there is nothing else of interest about the clock.")
                main()
            else:
                print("You do not have a screwdriver to unscrew the panel on the clock.")
                main()
        elif choice == 'n':
            main()
        else:
            print("Try again")
            self.insepct()

clock = Clock()

class Cupboard:
    def inspect(self):
        if cupboard_key not in player.inventory:
            print("There is a cupboard with a keyhole in the door.  The cupboard is locked.")
            main()
        else:
            print("You have unlocked the cupboard with the key you found under the plant pot.")
            choice = input("Would you like to interact with the contents of the cupboard? Type y/n: ")
            if choice == 'y':
                self.interact()
            elif choice == 'n':
                main()
            else:
                print("Try again")
                self.inspect()
    def interact(self):
        print("Inside the cupboard is a toolbox, and a framed picture.")
        choice = input("What would you like to interact with? Type \'toolbox\' or \'picture\': ")
        if choice == 'toolbox':
            if screwdriver not in player.inventory:
                print("You open the toolbox and find a screwdriver. You take the screwdriver.")
                player.inventory.append(screwdriver)
                self.inspect()
            else:
                print("You have taken the screwdriver and there is nothing else of interest in the toolbox.")
                self.inspect()
        elif choice == 'picture':
            print("The picture is of a man in a suit. You pick up the picture and turn it over to see the number 14 written on the back.")
            self.inspect()
        else:
            print("Try again")
            self.interact()

cupboard = Cupboard()

def main():
    inspect = input("What would you like to inspect? Type \'door\', \'desk\', \'cupboard\', \'clock\', \'shelf\' or \'plant\'.")
    if inspect == "door":
        door.inspect()
    elif inspect == 'desk':
        desk.inspect()
    elif inspect == 'cupboard':
        cupboard.inspect()
    elif inspect == 'clock':
        clock.inspect()
    elif inspect == 'shelf':
        shelf.inspect()
    elif inspect == 'plant':
        plant.inspect()
    else:
        print("Try again")
        main()
main()
