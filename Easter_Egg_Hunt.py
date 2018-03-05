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
                if player.coord == [row, col] and col == self.cols - 1:
                    print("|  p  |")
                elif player.coord == [row, col]:
                    print("|  p  ", end="")
                elif monster.coord == [row, col] and col == self.cols - 1:
                    print("|  m  |")
                elif monster.coord == [row, col]:
                    print("|  m  ", end="")
                elif basket.coord == [row, col] and col == self.cols - 1:
                    print("|  b  |")
                elif basket.coord == [row, col]:
                    print("|  b  ", end="")
                elif egg1.coord == [row, col] and col == self.cols - 1:
                    print("|  e  |")
                elif egg1.coord == [row, col]:
                    print("|  e  ", end="")
                elif egg2.coord == [row, col] and col == self.cols - 1:
                    print("|  e  |")
                elif egg2.coord == [row, col]:
                    print("|  e  ", end="")
                elif egg3.coord == [row, col] and col == self.cols - 1:
                    print("|  e  |")
                elif egg3.coord == [row, col]:
                    print("|  e  ", end="")
                elif door.coord == [row, col] and col == self.cols - 1:
                    print("|  d  |")
                elif door.coord == [row, col]:
                    print("|  d  ", end="")
                elif col == self.cols - 1:
                    print("|     |")
                else:
                    print("|     ", end="")
            if row == self.rows - 1:
                print("------" * self.rows)

    def checkGameOver(self, *args):
        if player.coord == monster.coord:
            clear_output()
            print("You ran into the monster! Sorry, but you lose. Better luck next time....")
            self.game_over = True
        elif player.coord == door.coord and basket.acquired and egg1.acquired and egg2.acquired and egg3.acquired:
            clear_output()
            print("Congratulations!! You beat the game!")
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

# Main loop
while stop == False:
    # Create instance of grid with pre-defined rows and cols
    rows = 6
    cols = 6
    grid = Grid(rows, cols)
    grid.initCoords()

    # Get random coords for objects
    random_coords = grid.getRandomCoords(7)

    # Create instances of objects
    player = Person(random_coords[0], 'Player', None)
    monster = Monster(random_coords[1], 'Monster', None)
    basket = Basket(random_coords[2], 'Basket', False)
    egg1 = Egg(random_coords[3], 'Egg 1', False)
    egg2 = Egg(random_coords[4], 'Egg 2', False)
    egg3 = Egg(random_coords[5], 'Egg 3', False)
    door = Door(random_coords[6], 'Door', None)


    # Initialize value for basket
    has_basket = False

    # Start main game loop
    while True:
        clear_output()
        print_instructions()
        basket.Acquired()
        egg1.Acquired()
        egg2.Acquired()
        egg3.Acquired()
        monster.changePosition(rows, cols)
        grid.drawGrid(player.coord, monster.coord, basket.coord, egg1.coord, egg2.coord, egg3.coord, door.coord)

        ans = input("What would you like to do? ")
        ans = ans.lower()

        if ans == 'q':
            clear_output()
            play_again = input("Would you like to play again? ")
            if play_again.lower() == 'yes':
                break
            else:
                stop = True
                break
        else:
            player.move_object(ans, rows, cols)

        # Check if player hits basket
        if has_basket == False:
            has_basket = grid.checkBasketAcquired(player.coord, basket.coord)

        # Check if player hits egg, if they have the basket already
        if has_basket == True:
            grid.checkEggAcquired(player.coord, egg1.coord, egg2.coord, egg3.coord)

        # Check if player hits monster
        game_over = grid.checkGameOver(player.coord, monster.coord, door.coord, egg1, egg2, egg3, basket)
        if game_over == True:
            play_again = input("Would you like to play again? ")
            if play_again.lower() == 'yes':
                break
            else:
                stop = True
                break
