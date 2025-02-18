class GameOf2048:
    collumn = []

        
        
    def flow_of_game(self):
        print(
            """
Commands are as follows : 
'W' or 'w' : Move Up
'S' or 's' : Move Down
'A' or 'a' : Move Left
'D' or 'd' : Move Right
              """)
        self.grid()
    
    def grid(self):
        for i in range(4):
            self.collumn.append([0] * 4)
        
        print(self.collumn)
        
def main():
    game = GameOf2048()
    game.flow_of_game()
    
if __name__ == "__main__":
    main()