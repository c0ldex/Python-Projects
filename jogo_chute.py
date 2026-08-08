import random

while True:
    try:
        # Get the level input
        level = int(input("Level: "))

        # If level is valid
        if level >= 1:
            # Generate a random number starting from 1 and ending at level
            number = random.randint(1, level)

            while True:
                try:
                    # Get the user's guess
                    guess = int(input("Guess: "))

                    if guess >= 1:
                        # If the guess in smaller then the number
                        if guess < number:
                            print("Too Small!")
                            # Make the user guess again
                            continue
                        elif guess > number:
                            # Make the user guess again
                            print("Too Large!")
                            continue
                        else:
                            print("Just right!")
                            # Leave the loop
                            break

                # If the guess is invalid, reprompt
                except ValueError:
                    pass
            # Leave the loop
            break
    # If the level is invalid, reprompt
    except ValueError:
        pass
