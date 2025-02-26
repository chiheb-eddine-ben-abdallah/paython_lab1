#gussing game from number 1 to 100
def gussing_game():
    num = int(45) #the number to guess
    while True: #loop until the number is guessed
        random_Num = int(input("Guess the number between 1 to 100: ")) 
        if random_Num < 1 or random_Num > 100: #if the number is out of range
            print("Try again --> Please enter a number between 1 to 100") 
        elif random_Num < num:
            print("to low!!!!!")
        elif random_Num > num:
            print("to high!!!!!")
        else:
            print("you win!!!!!!")
            break
        
gussing_game()