import random
import varsForNumbers
count = 1
random_number = random.randrange(1, 50)
hints_used = set()

while True :
    status = input("Enter 1 to play the game, enter 2 to see your stats, 3 to exit: ")
    if status == "1":
        while True:
            user_guess = int(input("Enter your guess: "))

            if count >= 5:
                print("You Lost :( The Number Was:", random_number)
                varsForNumbers.GamesPlayed += 1

                with open("varsForNumbers.py", "w") as f:
                    f.write(f"GamesPlayed = {varsForNumbers.GamesPlayed}\n")
                    f.write(f"score = {varsForNumbers.score}\n")
                    f.write(f"NumbersWon = {varsForNumbers.NumbersWon}\n")
                    break

            if user_guess == random_number:
                print("You Won!")
                print("1 score added to your points:")
                varsForNumbers.score += 1
                varsForNumbers.NumbersWon += 1
                varsForNumbers.GamesPlayed += 1

                with open("varsForNumbers.py", "w") as f:
                    f.write(f"GamesPlayed = {varsForNumbers.GamesPlayed}\n")
                    f.write(f"score = {varsForNumbers.score}\n")
                    f.write(f"NumbersWon = {varsForNumbers.NumbersWon}\n")
                    break
            elif user_guess > random_number:
                print("Your guess is high!")
            else:
                print("Your guess is low!")

            if varsForNumbers.score > 0:
                ask_hint = input("Do you want a hint? (yes/no): ").strip().lower()
                if ask_hint == "yes":
                    available_hints = ["parity", "prime"]
                    unused_hints = [hint for hint in available_hints if hint not in hints_used]

                    if not unused_hints:
                        print("You have already used all available hints!")
                    else:
                        hint = unused_hints[0]
                        hints_used.add(hint)
                        varsForNumbers.score -= 1
                        if count == 5:
                            print("You cant use hint in the last round")
                            break
                        else:
                            if hint == "parity":
                                print("Hint: The number is even" if random_number % 2 == 0 else "Hint: The number is odd")
                            elif hint == "prime":
                                for i in range(2, random_number):
                                    is_prime = True
                                    if random_number % i == 0:
                                        is_prime = False
                                        break
                                
                                print("Hint: The number is prime" if is_prime == True else "Hint: The number is not prime")
            else:
                print("You don't have enough score for a hint!")

            count += 1
            print("You have", 6 - count, "chances left.")

    elif status == "2":
        print("Total Games Played:", varsForNumbers.GamesPlayed)
        print("Total Wins:", varsForNumbers.NumbersWon)
        print("Total Score:", varsForNumbers.score)

    elif status == "3":
        break
    else : 
        print("Error")
