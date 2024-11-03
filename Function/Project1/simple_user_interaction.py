def display_game(game_list:list)->None:
    print("Here is the current List")
    print(game_list)

def position_choice()->int:
    choice = "wrong"

    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")

        if choice not in ['0', '1','2']:
            print("Invalid Choice")
    return int(choice)

def replacement_position(game_list: list, position: int)->list:
    replacement = input("Enter a string to place at postion: ")
    game_list[position] = replacement
    return game_list

def gameone_choice()->bool:
    choiche = "wrong"
    while choiche not in ['Y', 'N']:
        choiche = input("Do you want to Play again (Y / N): ").upper()

        if choiche not in ['Y', 'N']:
            print("Sorry I dont't understand, please enter (Y or N)")
    
    return True if choiche == "Y" else False

if __name__ == "__main__":
    game_one = True
    game_list = [1,2,3]

    while game_one:
        display_game(game_list)
        position = position_choice()
        game_list = replacement_position(game_list, position)
        display_game(game_list)
        game_one = gameone_choice()
        print("Thanks For playing !")
