import random

def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Invalid input. Please try again.")
        return False

    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("Your guess is out of range. Please try again")
        return False

    return True

def main():
    num_rand = random.randint(0, 100)
    score = 100

    while True:
       user_guess = input("Guesse a number between 1 and 100: ")
       if user_guess == "q":
        print('Thank you for playing.')
        break

       if not validate_input(user_guess):
        continue

       user_guess = int(user_guess)
       if num_rand > user_guess:
          print("Your guess is to low. Plase try again.")

       elif num_rand < user_guess:
          print("Your guess is to high. Please try again.")

       else:
        print("Congratulations! You guessed the correct number!")
        print(f"Your score is: {score} ")
        break

    score -= 10
    score = max(score, 0)


if __name__ == "__main__":
        main()
