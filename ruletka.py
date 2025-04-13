import random

RED_NUMBERS = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
BLACK_NUMBERS = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

def spin_wheel(): #spin the wheel!
    return random.randint(0, 36)

def get_color(number): #przypisanie kolorkow
    if number == 0:
        return "green"
    elif number in RED_NUMBERS:
        return "red"
    elif number in BLACK_NUMBERS:
        return "black"
    return None

def main():
    print("Welcome to the Roulette Game!")
    balance = 100
    while balance > 0:
        print(f"Your current balance is: ${balance}")
        try:
            bet = int(input("Enter your bet amount: "))
            if bet > balance or bet <= 0:
                print("Invalid bet amount.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        choice_type = input("Do you want to bet on a number or a color? (number/red/black/green): ").strip().lower()

        cheat_mode = False

        if choice_type == "number":
            try:
                number_choice_input = input("Pick a number between 0 and 36: ")

                if number_choice_input == "42":
                    print("😏 You discovered the cheat code! You will always win this round!")
                    cheat_mode = True
                    number_choice = 0  # anything, doesn't matter
                else:
                    number_choice = int(number_choice_input)
                    if number_choice < 0 or number_choice > 36:
                        print("Invalid number.")
                        continue
            except ValueError:
                print("Please enter a valid number.")
                continue
        elif choice_type not in ["red", "black", "green"]:
            print("Invalid choice. Please choose number, red, black, or green.")
            continue

        result = spin_wheel()
        result_color = get_color(result)

        if cheat_mode:
            result = number_choice
            result_color = get_color(result)

        print(f"The wheel landed on: {result} ({result_color})")

        #matma!
        if choice_type == "number" and (result == number_choice or cheat_mode):
            winnings = bet * 35
            print(f"You win! You earned ${winnings}")
            balance += winnings
        elif choice_type in ["red", "black"] and result_color == choice_type:
            winnings = bet * 2
            print(f"You win on color! You earned ${winnings}")
            balance += winnings
        elif choice_type == "green" and result == 0:
            winnings = bet * 30
            print(f"You win on green! You earned ${winnings}")
            balance += winnings
        else:
            print("You lose.")
            balance -= bet

        cont = input("Do you want to keep playing? (yes/no): ").lower()
        if cont != "yes":
            break

    print(f"Game over. Your final balance is: ${balance}")

if __name__ == "__main__":
    main()
