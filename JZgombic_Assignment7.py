#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import sys


random.seed(0)


class Player(object):

    def __init__(self, playerX):
        self.playerID = playerX
        self.roll = True
        self.total_score = 0

    def choice(self):

        try:
            choice = input("\nWhat would you like to do: Hold (h) or Roll (r)?")
            
            if choice not in ('h', 'r'):
                raise ValueError

            if choice.lower() == 'h':
                self.roll = False
                print ("\nYour have chosen to Hold. This ends your turn.\n")

            if choice.lower() == 'r':
                self.roll = True
                print ("Rolling.....\n")
                            
        except ValueError:
            print ("\nPlease enter a valid selection: h for Hold or r for Roll.\n")
            self.choice()


class Dice(object):

    def __init__(self):
        self.roll_value = None

    def roll(self):
        self.roll_value = random.randint(1, 6)
        return self.roll_value


class Continue(object):

    def __init__(self):
        self.proceed = False

    def replay(self):
        
        try:
            play = input("\n\nWould you like to play again: y for Yes or n for No  ")

            if play.lower() not in ('y', 'n'):
                raise ValueError

            if play.lower() == 'y':
                self.proceed = True

            if play.lower() == 'n':
                self.proceed = False

        except ValueError:
            print ("Please enter a valid selection: either y for Yes or n for No.")
            self.replay()


class Game(object):

    def __init__(self, playerNum):

        self.players = playerNum
        self.goal = 100

        self.first_player = random.randint(1, (len(self.players) - 1))
        self.next_player = None
        self.dice = Dice()
        self.play = Continue()

        self.current_player = self.players[self.first_player]
        print ("\nPlayer {} will go first\n".format(self.current_player.playerID))

        self.start_turn(self.current_player)


    def change_turn(self, player):

        if player.total_score >= self.goal:
            print ("\n\n          Player {} has won!!!!!!!!".format(player.playerID))
            print ("          Player {} has won!!!!!!!!".format(player.playerID))
            print ("          Player {} has won!!!!!!!!".format(player.playerID))
            self.play.replay()

            if self.play.proceed is True:
                main()

            if self.play.proceed is False:
                sys.exit

        else:
            if player.playerID == len(self.players):
                self.first_player = 0
                self.current_player = self.players[0]
                self.start_turn(self.current_player)
            else:
                self.first_player += 1
                self.current_player = self.players[self.first_player]
                self.start_turn(self.current_player)


    def start_turn(self, player):

        turn_score = 0
        count = len(self.players) - 1
        print ("     The updated scores are as follows:")

        while count >= 0:
            print ("          Player {} has {} points.".format(self.players[count].playerID, self.players[count].total_score))
            count -= 1

        print ("\n\n     Player {}:".format(player.playerID))

        player.roll = True
        
        while player.roll:
            die_num = self.dice.roll()

            if die_num == 1:
                print ("          You rolled a 1, your turn score is 0 and the next player will now roll.")
                player.roll = False

            elif (turn_score + player.total_score) >= self.goal:
                player.roll = False

            else:
                turn_score = turn_score + die_num
                print ("          You rolled a {} ".format(self.dice.roll_value))
                print ("          Your score for this round is {}".format(turn_score))
                print ("          Your total score for the game is {}".format(player.total_score))
                print ("          If you decide to hold, your total score will be {}".format((turn_score + player.total_score)))
                player.choice()

        player.total_score += turn_score
        print ("Your total score is now {}.".format(player.total_score))
        self.change_turn(player)
      

def main():

    number_of_players = int(input("\nPlease enter the number of players: "))

    if (number_of_players<2):
            print ("\nThis is not a one player game, please invite some friends!")
            main()
    else:
        try:
            number_of_players

        except ValueError:
            print ("Kindly input an integer.")
            main()

        players = []

        for num in range(number_of_players):
            players.append(Player(num + 1))

        Game(players)


if __name__ == '__main__':
    main()
