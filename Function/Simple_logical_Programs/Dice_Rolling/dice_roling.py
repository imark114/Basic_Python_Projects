from random import randint

def dice()->tuple:
    num1 = randint(1,6)
    num2 = randint(1,6)
    return(num1, num2)

def dice_rolling()->int:
    choice = ""
    cntn = True
    count = 0
    while cntn:
        while choice not in ['Y', 'N']:
            choice = input("Roll the dice? (Y / N) ").upper()
            if choice not in ['Y', 'N']:
                print("Please Enter (Y or N)")
            if choice == 'Y':
                num = int(input("How many time you want to dice the roll? "))
                while num > 0:
                    print(dice())
                    count+=1
                    num-=1
            else:
                cntn = False
        else:
            choice = ""
    return count

print("You've been rolled the dice:", dice_rolling(), "Time")
