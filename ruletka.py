
import random

def spin_wheel():
    return random.randint(0, 36)

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

        try:
            choice = int(input("Pick a number between 0 and 36: "))
            if choice < 0 or choice > 36:
                print("Invalid number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = spin_wheel()
        print(f"The wheel landed on: {result}")

        if result == choice:
            winnings = bet * 35
            print(f"You win! You earned ${winnings}")
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
