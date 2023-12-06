"""
Author: Hemil Patel (20013017), Kush Patel (20011282), Vaishvik Brahmbhatt (20011389)
Date: 5th dec 2023
Description: This is the main file where all the funtions are defined to read the csv file, move the captain 
vertically and horizontally, method to move the rabbit in any direction by one space, calculate the 
highscore when the game is completed and some other important funtions as well needed to run the code.
"""

import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
import os


class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    # This file will store the highscore data
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self._field = []
        self._rabbits = []
        self._captain = None
        self._veggies = []
        self._score = 0

    def initVeggies(self):
        # To check if the input is a valid file
        filename = input("Please enter the name of the vegetable point file: ")
        while not os.path.exists(filename):
            print("File not found. Please enter a valid filename.")
            filename = input("Please enter the name of the vegetable point file: ")

        # Reads the first line and gets the dimensions from the csv file
        with open(filename, 'r') as file:
            var1, var2 = file.readline().split()
            x, height, width = var2.split(',')
            height = int(height)
            width = int(width)
            self._field = [[None for _ in range(width)] for _ in range(height)]

            # Read remaining lines to create Veggie objects and populate the field
            for line in file:
                veggie_data = line.strip().split(',')
                veggie = Veggie(veggie_data[0], veggie_data[1], int(veggie_data[2]))
                self._veggies.append(veggie)

            inserted_veggies = 0
            # Place veggie in a random location
            while inserted_veggies < self.NUMBEROFVEGGIES:
                x, y = random.randint(0, height - 1), random.randint(0, width - 1)
                if self._field[x][y] is None:
                    self._field[x][y] = random.choice(self._veggies)
                    inserted_veggies += 1
        # Close the file
        file.close()

    # Method to initialize captain at some random coordinate        
    def initCaptain(self):
        while True:
            x, y = random.randint(0, len(self._field) - 1), random.randint(0, len(self._field[0]) - 1)
            if self._field[x][y] is None:
                self._captain = Captain(x, y)
                self._field[x][y] = self._captain
                break

    def initRabbits(self):
        height, width = len(self._field), len(self._field[0])

        for _ in range(self.NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, height - 1), random.randint(0, width - 1)
                if self._field[x][y] is None:
                    rabbit = Rabbit(x, y)
                    self._rabbits.append(rabbit)
                    self._field[x][y] = rabbit
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        count = 0
        for row in self._field:
            for cell in row:
                if cell is not None and cell._symbol not in ('R', 'V'):
                    count += 1
        return count

    def intro(self):
        print("Welcome to Captain Veggie! \n")
        print("The rabbits have invaded your garden and you must harvest as many vegetables as possible before the "
              "rabbits eat them all! Each vegetable is worth a different number of points so go for the high score! "
              "\n")
        print("List of possible vegetables:")
        for veggie in self._veggies:
            print(veggie)
        print("\n")
        print("Captain Veggie is V, and the rabbits are R's.")
        print("Good luck! \n")

    def printField(self):
        #This will print the grid with positions of all the vegetables, rabbits and captain.
        cols = len(self._field[0])
        print('#' * (cols * 3 + 2))
        for row in self._field:
            row_str = "#"
            for cell in row:
                if cell is not None:
                    row_str += f" {cell._symbol} "
                else:
                    row_str += "   "
            row_str += "#"
            print(row_str)
        print('#' * (cols * 3 + 2))

    def getScore(self):
        return self._score

    def moveRabbits(self):
        for rabbit in self._rabbits:
            current_row, current_col = rabbit.get_x(), rabbit.get_y()

            # Calculate random movement direction
            movement_row = random.choice([-1, 0, 1])
            movement_col = random.choice([-1, 0, 1])

            # Calculate the new position after movement
            new_row, new_col = current_row + movement_row, current_col + movement_col

            # Check if the new position is within the boundaries of the field
            if 0 <= new_row < len(self._field) and 0 <= new_col < len(self._field[0]):
                # Check if the new position is an empty slot
                if self._field[new_row][new_col] is None:
                    # Update Rabbit's variables
                    rabbit.set_x(new_row)
                    rabbit.set_y(new_col)
                    # Assign Rabbit to the new location in the field
                    self._field[new_row][new_col] = rabbit
                    # Set the previous location in the field to None
                    self._field[current_row][current_col] = None
                else:
                    # Check if the new position is occupied by a Captain object or another Rabbit object
                    if isinstance(self._field[new_row][new_col], (Captain, Rabbit)):
                        # Rabbit forfeits its move
                        pass
                    # Check if the new position is occupied by a Veggie object
                    elif isinstance(self._field[new_row][new_col], Veggie):
                        # Remove the Veggie object from the field
                        self._field[current_row][current_col] = None
                        # Rabbit takes the place of the Veggie in the field
                        self._field[new_row][new_col] = rabbit
                        # Update Rabbit's variables
                        rabbit.set_x(new_row)
                        rabbit.set_y(new_col)
                        # Set the previous location in the field to None
                        self._field[current_row][current_col] = None

    def moveCptVertical(self, movement):
        current_x, current_y = self._captain.get_x(), self._captain.get_y()
        new_x = current_x + movement

        if 0 <= new_x < len(self._field) and self._field[new_x][current_y] is None:
            # Move successful
            self._field[new_x][current_y] = self._captain
            self._field[current_x][current_y] = None
            self._captain.set_x(new_x)
        elif 0 <= new_x < len(self._field) and isinstance(self._field[new_x][current_y], Veggie):
            # Veggie found
            veggie = self._field[new_x][current_y]
            self._captain.add_veggie(veggie)
            self._score += veggie.get_points()
            print(f"Captain found a delicious vegetable: {veggie.get_name()} worth {veggie.get_points()} points!")
            self._field[new_x][current_y] = self._captain
            self._field[current_x][current_y] = None
            self._captain.set_x(new_x)
        elif 0 <= new_x < len(self._field) and isinstance(self._field[new_x][current_y], Rabbit):
            print("Don't step on the bunnies! Move blocked.")
        else:
            print("You can't move that way! Move blocked.")

    def moveCptHorizontal(self, movement):
        current_x, current_y = self._captain.get_x(), self._captain.get_y()
        new_y = current_y + movement

        if 0 <= new_y < len(self._field[0]) and self._field[current_x][new_y] is None:
            # Move successful
            self._field[current_x][new_y] = self._captain
            self._field[current_x][current_y] = None
            self._captain.set_y(new_y)
        elif 0 <= new_y < len(self._field[0]) and isinstance(self._field[current_x][new_y], Veggie):
            # Veggie found
            veggie = self._field[current_x][new_y]
            self._captain.add_veggie(veggie)
            self._score += veggie.get_points()
            print(f"Captain found a delicious vegetable: {veggie.get_name()} worth {veggie.get_points()} points!")
            self._field[current_x][new_y] = self._captain
            self._field[current_x][current_y] = None
            self._captain.set_y(new_y)
        elif 0 <= new_y < len(self._field[0]) and isinstance(self._field[current_x][new_y], Rabbit):
            print("Don't step on the bunnies! Move blocked.")
        else:
            print("You can't move that way! Move blocked.")

    # Method to get the input from the user and based on that move the captain in that direction
    def moveCaptain(self):
        direction = input("Enter direction to move Captain (W/A/S/D): ").lower()
        if direction == 'w':
            self.moveCptVertical(-1)
        elif direction == 's':
            self.moveCptVertical(1)
        elif direction == 'a':
            self.moveCptHorizontal(-1)
        elif direction == 'd':
            self.moveCptHorizontal(1)
        else:
            print("Invalid input. Please enter W, A, S, or D.")


def gameOver(self):
    print("Game Over!")
    print("Vegetables harvested by Captain:")
    for veggie in self._captain.get_veggies_collected():
        print(veggie.get_name())
    print("Final Score:", self._score)


def highScore(self):
    # Declare an empty List to store Tuples representing player initials and their score
    high_scores = []

    # Check if the highscore.data file exists
    if os.path.exists(self.HIGHSCOREFILE):
        # Open the file for binary reading
        with open(self.HIGHSCOREFILE, 'rb') as file:
            # Unpickle the file into the List of high scores
            high_scores = pickle.load(file)

    # Prompt the user for their initials and extract the first 3 characters
    player_initials = input("Enter your initials (3 characters): ").upper()[:3]

    # Create a Tuple with the player’s initials and score
    player_score = self.getScore()
    player_tuple = (player_initials, player_score)

    # Add the player's Tuple to the List of high scores
    if not high_scores:
        high_scores.append(player_tuple)
    else:
        # Add the player's Tuple to the correct position in the List
        inserted = False
        for i, (initials, score) in enumerate(high_scores):
            if player_score > score:
                high_scores.insert(i, player_tuple)
                inserted = True
                break

        # If the player's score is not greater than any existing scores, append it to the end
        if not inserted:
            high_scores.append(player_tuple)

    # Output all the high scores in the List, with an appropriate header
    print("\nHigh Scores:")
    for i, (initials, score) in enumerate(high_scores):
        print(f"{i + 1}. {initials}: {score}")

    # Open the highscore.data file for binary writing
    with open(self.HIGHSCOREFILE, 'wb') as file:
        # Pickle the List of high scores to the file
        pickle.dump(high_scores, file)

    # Close the file
    file.close()
