"""
Author: Hemil Patel (20013017)
Date: 5th dec 2023
Description: Main file that creates game_engine object and displays the game introduction using appropriate 
GameEngine funtion. It also prints out the field using the printField method moves the rabbit and captain
using moveRabbits and moveCaptain funtions. It also displays the when game is over and displays Highscore at the 
end. 
"""

from GE import GameEngine

def main():
    
    # Instantiate and store a GameEngine object
    game_engine = GameEngine()

    # Initialize the game
    game_engine.initializeGame()

    # Display the game’s introduction
    game_engine.intro()

    # Create a variable to store the number of remaining vegetables
    remaining_veggies = game_engine.remainingVeggies()

    # Main game loop
    while remaining_veggies > 0:
        # Output the number of remaining vegetables and the player’s score
        print(f"Remaining Vegetables: {remaining_veggies} | Score: {game_engine.getScore()}")

        # Print out the field
        game_engine.printField()

        # Move the rabbits
        game_engine.moveRabbits()

        # Move the captain
        game_engine.moveCaptain()

        # Determine the new number of remaining vegetables
        remaining_veggies = game_engine.remainingVeggies()

    # Display the Game Over information
    game_engine.gameOver()

    # Handle the High Score functionality
    game_engine.highScore()

if __name__ == "__main__":
    main()
