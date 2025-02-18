import random

class RockPaperScissors:
    rock: str = "Rock"
    paper: str = "Paper"
    scissors: str = "Scissors"
    
    player_choice_int: int = 0
    computer_choice_int: int = 0

    players_choice: str = ""
    computers_choice: str = ""

    result: str = ""
    winner = ""
    wins = []
    def flow_of_game(self):
        while True:
            print(
            """Winning rules of the game ROCK PAPER SCISSORS are:
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins
    """
            )
            print(
                """
Enter your choice 
1 - Rock 
2 - Paper 
3 - Scissors 
    """
            )
            
            self.getting_input()
            
            print(self.players_choice + " vs " + self.computers_choice)
            
            self.way_vs_way()
            self.determine_winner()
            
            self.wins.append((self.winner, self.result, self.players_choice, self.computers_choice))
            for i, win in enumerate(self.wins):
                print(f"Game {i + 1}: Result - {win[0]} with {win[1]}, Player's choice - {win[2]}, Computer's choice - {win[3]}")
            
            want_to_break = input("Do you want to go again (Y/n): ").strip().lower()
            if want_to_break == "y":
                continue
            else:
                print("Thank you for playing this game")
                break

    def assigning(self, way, player):
        if player:
            if way == 1:
                self.players_choice = self.rock
            elif way == 2:
                self.players_choice = self.paper
            elif way == 3:
                self.players_choice = self.scissors
        else:
            if way == 1:
                self.computers_choice = self.rock
            elif way == 2:
                self.computers_choice = self.paper
            elif way == 3:
                self.computers_choice = self.scissors

    def getting_input(self):
        while True:
            self.player_choice_int = int(input("Enter your choice: "))

            if self.player_choice_int < 1 or self.player_choice_int > 3:
                print("Please enter a valid single number.")
                continue

            self.assigning(self.player_choice_int, True)
            print("User choice is:", self.players_choice)

            self.generate_computer_choice()
            self.assigning(self.computer_choice_int, False)
            print("Computer choice is:", self.computers_choice)

            break
        

    def generate_computer_choice(self):
        choice = random.randint(1, 3)
        self.computer_choice_int = choice

    def way_vs_way(self):
        if self.player_choice_int == self.computer_choice_int:
            self.result = "Draw"
        elif (self.player_choice_int == 1 and self.computer_choice_int == 2) or (self.player_choice_int == 2 and self.computer_choice_int == 1):
            self.result = "Paper"
        elif (self.player_choice_int == 1 and self.computer_choice_int == 3) or (self.player_choice_int == 3 and self.computer_choice_int == 1):
            self.result = "Rock"
        elif (self.player_choice_int == 3 and self.computer_choice_int == 2) or (self.player_choice_int == 2 and self.computer_choice_int == 3):
            self.result = "Scissors"

    def determine_winner(self):
        if self.result == "Draw":
            print("<======== It's a tie! ========>")
            self.winner = "draw"
        elif self.result == self.players_choice:
            print("<======== User wins! ========>")
            self.winner = "user"
        else:
            print("<======== Computer wins! ========>")
            self.winner = "computer"
            

def main():
    game = RockPaperScissors()
    game.flow_of_game()

if __name__ == "__main__":
    main()
