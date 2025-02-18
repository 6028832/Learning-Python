import datetime
import requests

class WordGuessing:
    name:str = ""
    date:str = datetime.datetime.now().strftime("%Y-%m-%d")
    solution:str = ""
    amounts_of_guesses:int = 8
    guessed_letter:str = ""
    
    def beginning_game(self):   
        print("Fill in the name")
        self.name = str(input())
        print("Welcome to this game of guessing the word", self.name)
    
    def getting_the_word(self):
        # https://www.nytimes.com/svc/wordle/v2/2024-12-24.json
        try:
            response = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{self.date}.json").json()
            self.solution = response.get('solution')            
        except:
            return
        
        return
    
    def guessing_word(self):
        revealed = ["-" for _ in self.solution]
        
        while self.amounts_of_guesses > 0:
            print("What letter do you think the word contains?")
            guess = str(input()).lower()  
            
            if len(guess) != 1:
                print("Please enter a valid single letter.")
                continue
            
            self.guessed_letter += guess
            found_match = False

            for i, character in enumerate(self.solution):
                if character == guess:
                    revealed[i] = character
                    found_match = True

            if not found_match:
                self.amounts_of_guesses -= 1
                print(f"Wrong guess! You have {self.amounts_of_guesses} guesses left.")
            else:
                print("Correct guess!")

            # Display the current state of the word
            print(" ".join(revealed))
            
            # Check if the player has guessed the full word
            if "-" not in revealed:
                print(f"Congratulations {self.name}! You guessed the word: {self.solution}")
                return

        print(f"Game over! The word was: {self.solution}")
    
    
    
def main():
    game = WordGuessing()
    game.beginning_game()
    game.getting_the_word()
    game.guessing_word()
    

if __name__ == "__main__":
    main()