import random

class GuessingGame:
    min_number:int = 0
    max_number:int = 0
    end_number: int = 0
    guessed_try:int = 0
    amount_of_tries:list = []
    
    def trying_to_input(self):
        while True:
            try:
                return int(input())
            except ValueError:
                print("try again and fill in the value correct this time")
         
    def take_terminal_input(self):
        while True:
            print("Type the numbers for the game and it must be a number")
            try:
                
                print("Type the minimum number for the game:")
                self.min_number = self.trying_to_input()
                print("Type the maximum number for the game:")
                self.max_number = self.trying_to_input()
                if self.min_number > self.max_number:
                    print("The minimum number must be less than the maximum number")
            except ValueError:
                print("Please enter valid integers.")


    def get_random_number(self):
        random_value = random.randint(self.min_number, self.max_number)
        self.end_number = random_value
        
        return

    def guessing_the_number(self):
        while True:
            print("Type the number you think it is")
            guessed_number = int(input())
            self.guessed_try = guessed_number
            if self.end_number == self.guessed_try:
                print("The number you have guessed is right !!!")
                self.amount_of_tries.append(self.guessed_try)
                break
            elif self.end_number < self.guessed_try:
                print("Try Again! You guessed too high")
                self.amount_of_tries.append(self.guessed_try)
            elif self.end_number > self.guessed_try:
                print("Try Again! You guessed too low")
                self.amount_of_tries.append(self.guessed_try)
        print("Amount of tries to get this right:", len(self.amount_of_tries))
        for tries in self.amount_of_tries:
            print(f"Try: {tries}")
        return
        
def main():
    game = GuessingGame()
    game.take_terminal_input()
    game.get_random_number()
    game.guessing_the_number()

if __name__ == "__main__":
    main()