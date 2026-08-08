# Importing the random librarie
import random

def main():
    # Level variable and its value will be the returned value of get_level()
    level = get_level()

    # Start the score from 0
    score = 0

    # Ask 10 questions
    for i in range(10):
        # Generating each number for that question
        x = generate_integer(level)
        y = generate_integer(level)

        # Making sure the user has 3 tries for each question
        tries = 0
        # Calculating the result of that question
        result = x + y

        while tries < 3:
            try:
                # Get the user's answer
                answer = int(input((f"{x} + {y} = ")))
                if answer == result:
                    # Add 1 to the score
                    score += 1
                    break
                # If the answer is not matching with the result
                else:
                    # Add a try
                    tries += 1
                    print("EEE")
            # If the user dosent type a integer
            except ValueError:
                tries += 1
                print("EEE")

        # If the user has 3 tries then
        if tries == 3:
            # Print the result
            print(f"{x} + {y} = {result}")

    # At the end of all 10 questions show the user its score
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            # Get user's input
            level = int(input("Level: "))

            # Check ff the level is from 1 to 3
            if level < 1 or level > 3:
                # Raise a error so the try makes the user retype
                raise ValueError

            # If no problems were found return the level
            return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        # Generate a ramdom number from 0 to 9
        return random.randint(0, 9)
    elif level == 2:
        # Generate a ramdom number from 10 to 99
        return random.randint(10, 99)
    elif level == 3:
        # Generate a ramdom number from 100 to 999
        return random.randint(100, 999)
    else:
        # Give a error witch is impossible since this func only runs based on the level, but why not
        raise ValueError

if __name__ == "__main__":
    main()
