

import random

def get_optimal_attempts(target, low, high):
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid == target:
            return count
        
        elif mid < target:
            low = mid + 1
        
        else:
            high = mid - 1
    return count

def get_rank(user_attempts, optimal_attempts):
    diff = user_attempts - optimal_attempts
    if diff <= 0:
        return "LEGENDARY (Perfect Strategy!)"
    
    elif diff == 1:
        return "MASTER (Very Close!)"
    
    elif diff <= 3:
        return "PRO (Good Job!)"
    
    else:
        return "APPRENTICE (Keep Practicing!)"

def computer_guesses():
    print("\n" + "-" * 40)
    print(" MODE: COMPUTER GUESSES YOUR NUMBER ".center(40, "-"))
    print("Think of a number between (1 - 100).")
    
    low, high, attempts = 1, 100, 0
    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        print(f"\nAttempt {attempts}: Is your number {mid}?")
        print(f"Is your secret number (Greater) than {mid}, (Smaller) than {mid}, or (True)?")
        
        feedback = input("Your answer: ").strip().lower()
        if feedback == "true":
            print(f"\nVictory! I guessed it in {attempts} attempts.")
            break
        
        elif feedback == "greater":
            low = mid + 1
        
        elif feedback == "smaller":
            high = mid - 1
        
        else:
            print("Invalid input, please try again.")
            attempts -= 1
            
        if low > high:
            print("\nWait! Your hints are contradictory. I can't guess the number!")
            break

def user_guesses():
    print("\n" + "-" * 40)
    print(" MODE: YOU GUESS THE COMPUTER'S NUMBER ".center(40, "-"))
    
    target = random.randint(1, 100)
    optimal = get_optimal_attempts(target, 1, 100)
    attempts = 0
    guess = 0
    
    print(f"I've picked a secret number. Try to beat the optimal score: {optimal} attempts!")
    
    while guess != target:
        try:
            guess = int(input("\nGuess a number (1-100): "))
            attempts += 1
            
            if guess < target:
                print("Too low! Try a greater number.")
            
            elif guess > target:
                print("Too high! Try a smaller number.")
            
            else:
                rank = get_rank(attempts, optimal)
                print("\n" + "* "* 30)
                print(f" EXCELLENT! ".center(30, "*"))
                print(f"The number was: {target}\nYour attempts: {attempts}\nOptimal needed: {optimal}\nRank: {rank}")
                print("*" * 30)
        
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n" + "*" * 45)
        print(" WELCOME TO THE GUESS GAME ".center(45, "*"))
        print("*" * 45)

        print("1. Computer guesses your number")
        print("2. You guess the computer's number (Challenge Mode)")
        print("3. Exit")
        
        choice = input("\nChoose an option (1/2/3): ").strip()
        if choice == '1':
            computer_guesses()
        
        elif choice == '2':
            user_guesses()
        
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        
        else:
            print("Invalid choice, please select 1, 2, or 3.")
            continue
        
        print("\n" + "-" * 30)
        again = input("What's next? (Play again / Change mode / Exit): ").strip().lower()
        if again == "exit":
            print("Goodbye!")
            break
        
        elif again == "change mode":
            continue

        
        elif again == "play again":
            if choice == '1':
              computer_guesses()
            else:
              user_guesses()
        
        else:
            print("Invalid choice, please select (Play again / Change mode / Exit).")

main()
