from random import randint

def random_number(mini: int, maxi: int)->int:
    return randint(mini, maxi)

def guess_num():
    mini = int(input("Enter the Minimum number of the range: "))
    maxi = int(input("Enter the maximum number of the range: "))
    attmpts = 0
    chance = int((mini + maxi) * 0.07)
    ran_num = random_number(mini, maxi)
    print(f"You've {chance} Chance to guess the number")
    while chance > 0:
        guess = int(input("Guess the number: "))
        attmpts +=1
        if guess == ran_num:
            print("Congratulation Your guess correct")
            return attmpts
        elif guess > ran_num:
            print("Too high! Try again")
            chance-=1
        else:
            print("Too low! Try again")
            chance-=1
    return None
        
def play_game():
    rslt = guess_num()
    attempts = [rslt]
    choice = ''
    cntn = True
    while cntn:
        while choice not in ['Y', 'N']:
            choice = input("Do you want to play again? (Y / N): ").upper()
            if choice not in ['Y', 'N']:
                print("Please Enter (Y or N)")
            if choice == 'Y':
                rslt = guess_num()
                attempts.append(rslt)
            else:
                cntn = False
        else:
            choice = ""
    return attempts


if __name__ == "__main__":
    print("---------------------")
    print("Welcome to number guessing game!!!")
    result = play_game()
    own = list(filter(lambda num: num !=None, result))
    print(f"You've been palyedd the game {len(result)} times")
    print(f"You've been own {len(own)} times")
    print(f"Your best score: {min(own) if len(own) > 0 else 0}")