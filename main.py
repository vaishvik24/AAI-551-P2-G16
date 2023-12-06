"""
Author: Hemil Patel (20013017)
Date: 5th dec 2023
Description: Main file that creates game_engine object and displays the game introduction using appropriate 
GameEngine funtion. It also prints out the field using the printField method moves the rabbit and captain
using moveRabbits and moveCaptain funtions. It also displays the when game is over and displays Highscore at the 
end. 
"""

from GameEngine import GameEngine


def main():
    # init GameEngine object
    game_engine = GameEngine()

    # starts game
    game_engine.initializeGame()

    # prints intro msg
    game_engine.intro()

    # fetches remaining veggies in the current field stage
    remaining_veggies = game_engine.remainingVeggies()

    while remaining_veggies > 0:
        # prints current state
        print(f"Remaining Vegetables: {remaining_veggies} | Score: {game_engine.getScore()}")
        game_engine.printField()

        # move rabbits
        game_engine.moveRabbits()

        # move captain as per user commnad
        game_engine.moveCaptain()

        # updates new veggies after changes
        remaining_veggies = game_engine.remainingVeggies()

    # terminate the game and display final o/p
    game_engine.gameOver()

    # prints out data result file
    game_engine.highScore()


if __name__ == "__main__":
    main()
