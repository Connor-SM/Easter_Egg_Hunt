from IPython.display import clear_output
import random

# Create class for objects in game
class EasterObj():
    def __init__(self, coord, name, acquired):
        self.coord = coord
        self.name = name
        self.acquired = acquired

    def getCoord(self):
        return self.coord

    def setCoord(self, coord):
        self.coord = coord

    def printPosition(self):
        print("{} is at position: {}".format(self.name, self.coord))


class Person(EasterObj):
    def move_object(self, move, rows, cols):
        if move == 'right':
            if self.coord[1] >= cols - 1:
                return
            else:
                self.coord[1] += 1
        elif move == 'up':
            if self.coord[0] <= 0:
                return
            else:
                self.coord[0] -= 1
        elif move == 'down':
            if self.coord[0] >= rows - 1:
                return
            else:
                self.coord[0] += 1
        elif move == 'left':
            if self.coord[1] <= 0:
                return
            else:
                self.coord[1] -= 1


class Monster(EasterObj):
    # For later use to follow the player
    def changePosition(self, rows, cols):
        self.coord[0] = random.randint(0, rows - 1)
        self.coord[1] = random.randint(0, cols - 1)


class Basket(EasterObj):
    def Acquired(self):
        if self.acquired == False:
            print("Goal: You haven't acquired the basket yet!")
        else:
            self.coord = [-1, -1]
            print("You've acquired the basket!")


class Egg(EasterObj):
    def Acquired(self):
        if self.acquired == False:
            print("Goal: You haven't acquired {} yet!".format(self.name))
        else:
            self.coord = [-1, -1]
            print("You've acquired {}!".format(self.name))


class Door(EasterObj):
    def changeLocation(self):
        return


class Game_Manager():
    def __init__(self, level, turn):
        self.level = level
        self.turn = turn

    def display_game_info(self, numMonsters):
        print("Level = {}\nTurn = {}\nNumber of Monsters = {}".format(self.level, self.turn, numMonsters))


class Grid():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.coords = []
        self.game_over = False

    def initCoords(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.coords.append([row, col])

    def getCoords(self):
        return self.coords

    def getRandomCoords(self, num_obj):
        return random.sample(self.coords, num_obj)


    def drawGrid(self, *args):
        for row in range(self.rows):
            print("------" * self.rows)
            for col in range(self.cols):
                flag = False
                # Create monsters on grid with for loop
                for monster_coord in monster_coords:
                    if monster_coord == [row, col] and col == self.cols - 1 and flag == False:
                        print("|  m  |")
                        flag = True
                    elif monster_coord == [row, col] and flag == False:
                        flag = True
                        print("|  m  ", end="")
                if player.coord == [row, col] and col == self.cols - 1 and flag == False:
                    print("|  p  |")
                elif player.coord == [row, col] and flag == False:
                    print("|  p  ", end="")
                elif basket.coord == [row, col] and col == self.cols - 1 and flag == False:
                    print("|  b  |")
                elif basket.coord == [row, col] and flag == False:
                    print("|  b  ", end="")
                elif egg1.coord == [row, col] and col == self.cols - 1 and flag == False:
                    print("|  e  |")
                elif egg1.coord == [row, col] and flag == False:
                    print("|  e  ", end="")
                elif egg2.coord == [row, col] and col == self.cols - 1 and flag == False:
                    print("|  e  |")
                elif egg2.coord == [row, col] and flag == False:
                    print("|  e  ", end="")
                elif egg3.coord == [row, col] and col == self.cols - 1 and flag == False:
                    print("|  e  |")
                elif egg3.coord == [row, col] and flag == False:
                    print("|  e  ", end="")
                elif door.coord == [row, col] and col == self.cols - 1 and flag == False:
                    print("|  d  |")
                elif door.coord == [row, col] and flag == False:
                    print("|  d  ", end="")
                elif col == self.cols - 1 and flag == False:
                    print("|     |")
                elif flag == False:
                    print("|     ", end="")
            if row == self.rows - 1:
                print("------" * self.rows)

    def checkGameOver(self, *args):
        for monster_coord in monster_coords:
            if player.coord == monster_coord:
                clear_output()
                print("Monster that killed you was at {}, and you were at {}".format(monster_coord, player.coord))
                print("You ran into the monster! Sorry, but you lose. Better luck next time....")
                print("You managed to make it to level {} before dying. ".format(game_manager.level) +
                      "You faced a max of {} monster(s).".format(len(monster_coords)))
                game_manager.level = 1
                game_manager.turn = 0
                self.game_over = True
        if player.coord == door.coord and basket.acquired and egg1.acquired and egg2.acquired and egg3.acquired:
            clear_output()
            print("Congratulations!! You beat the game!")
            game_manager.level += 1
            game_manager.turn = 0
            self.game_over = True
        return self.game_over

    def checkBasketAcquired(self, *args):
        if player.coord == basket.coord:
            basket.acquired = True
            return True
        return False

    def checkEggAcquired(self, *args):
        if player.coord == egg1.coord:
            egg1.acquired = True
        if player.coord == egg2.coord:
            egg2.acquired = True
        if player.coord == egg3.coord:
            egg3.acquired = True



# Display Instructions
def print_instructions():
    print("Welcome to the Easter Egg Hunt!!\n\n")
    print("How To Play")
    print("================================")
    print("1) You must exit the room through the door (displayed as 'd').")
    print("2) However, the door will not open until you collect all of the eggs (displayed as 'e'.)")
    print("3) In order to collect the eggs, you must first pickup the basket (displayed as 'b'.)")
    print("4) You are displayed as 'p' and can move by entering 'left', 'right', 'up', or 'down' (press 'q' to quit)")
    print("5) If you run into the monster (displayed as 'm') you will lose the game!")
    print("================================")
    print("Good luck!\n")


# Main loop flag
stop = False
# Game manager object, put main loop flag in later
game_manager = Game_Manager(1, 0)

# Main loop
while stop == False:
    # Create instance of grid with pre-defined rows and cols
    rows = 6
    cols = 6
    grid = Grid(rows, cols)
    grid.initCoords()

    # Initialize levels and empty monster list
    monsters = []

    # Get random coords for objects
    random_coords = grid.getRandomCoords(6 + game_manager.level)

    # Create instances of objects
    player = Person(random_coords[0], 'Player', None)
    basket = Basket(random_coords[1], 'Basket', False)
    door = Door(random_coords[2], 'Door', None)
    egg1 = Egg(random_coords[3], 'Egg 1', False)
    egg2 = Egg(random_coords[4], 'Egg 2', False)
    egg3 = Egg(random_coords[5], 'Egg 3', False)
    #monster = Monster(random_coords[6], 'Tiger', None)

    # Create Monster instances based on list
    for i in range(game_manager.level):
        monsters.append(Monster(random_coords[i + 6], 'Monster', None))

    # Create variable for monster coords
    monster_coords = []

    for monster in monsters:
        monster_coords.append(monster.coord)

    # Initialize value for basket
    has_basket = False

    # Start main game loop
    while True:
        game_over = False
        game_manager.turn += 1
        clear_output()
        print_instructions()
        game_manager.display_game_info(len(monster_coords))

        # Check if player hits basket
        if has_basket == False:
            has_basket = grid.checkBasketAcquired(player.coord, basket.coord)

        # Check if player hits egg, if they have the basket already
        if has_basket == True:
            grid.checkEggAcquired(player.coord, egg1.coord, egg2.coord, egg3.coord)

        # Print acquired correctly
        basket.Acquired()
        egg1.Acquired()
        egg2.Acquired()
        egg3.Acquired()

        # Check if player hits monster before everything else
        if game_manager.turn > 2:
            game_over = grid.checkGameOver(player.coord, monster_coords, door.coord, egg1, egg2, egg3, basket, game_manager)

        if game_over == False:
            # Change all monsters positions
            for monster in monsters:
                monster.changePosition(rows, cols)

            grid.drawGrid(player.coord, monster_coords, basket.coord, egg1.coord, egg2.coord, egg3.coord, door.coord)

            # Check if player hits monster before everything else
            if game_manager.turn > 1:
                game_over = grid.checkGameOver(player.coord, monster_coords,
                                               door.coord, egg1, egg2, egg3, basket, game_manager)

        if game_over == True:
            play_again = input("Would you like to play again? ")
            if play_again.lower() == 'yes':
                game_manager.turn = 0
                break
            else:
                stop = True
                break
        else:
            ans = input("What would you like to do? ")
            ans = ans.lower()

        if ans == 'q':
            play_again = input("Would you like to play again? ")
            if play_again.lower() == 'yes':
                game_manager.turn = 0
                break
            else:
                stop = True
                break
        else:
            player.move_object(ans, rows, cols)
