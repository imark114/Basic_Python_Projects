from random import choice
choices = ('r', 'p', 's')
def user_choice()->str:
    user_ch = ''
    while user_ch not in choices:
        user_ch = input("Rock, Paper, Scissor? (R / P / S): ").lower()
        if user_ch not in choices:
            print("Invalid Choice")
    return user_ch

def chek_win() ->str:
    emoji = {'r': '🪨', 'p': '📑', 's': '✀'}
    user_ch = user_choice()
    print(f"You Chose {emoji[user_ch]}")
    computer_ch = choice(choices)
    print(f"Computer Chose {emoji[computer_ch]}")
    if user_ch == computer_ch:
        print("Tie")
        return "tie"
    elif (user_ch == 'r' and computer_ch == 's') or (user_ch == 'p' and computer_ch == 'r') or (user_ch == 's' and computer_ch == 'p'):
        print("You Win!!")
        return "win"
    else:
        print("Computer Win!!")
        return "loss"

def play_game() ->list:
    status = [chek_win()]
    chs = ''
    cntn = True
    while cntn:
        while chs not in ('Y', 'N'):
            chs = input("Play again? (Y / N): ").upper()
            if chs not in ('Y', 'N'):
                print("Please press (Y or N)")
            if chs == 'Y':
                status.append(chek_win())
            else:
                cntn = False
        else:
            chs = ""
    return status

if __name__ == "__main__":
    result = play_game()
    played = len(result)
    print(f"You've been played the game {played} times")

    if played == 3:
        count = 0
        count2 = 0
        for sts in result:
            if sts == 'tie':
                continue
            elif sts == 'win':
                count+=1
            else:
                count2 +=1
        if 1 < count <= 3:
            print("Over all You win")
        elif 1 <count2 <=3:
            print("Over all Computer win")
        else:
            print("Over all Tie")

    elif played > 1:
        tie = 0
        win = 0
        loss = 0
        for sts in result:
            if sts == 'loss':
                loss+=1
            elif sts == 'win':
                win+=1
            else:
                tie+=1

        print(f"You tied {tie} times")
        print(f"You won {win} times")
        print(f"You lossed {loss} times")
