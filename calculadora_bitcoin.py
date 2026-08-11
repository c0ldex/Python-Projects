# Importing the libraries
import sys
import requests

# If the user inputed 2 arguments in the command line
if len(sys.argv) == 2:
    try:
        # Try to convert the 1's argument as a float
        bitcoins = float(sys.argv[1])

    except ValueError:
        # If the conversion failed, exit the program
        sys.exit("Command-line argument is not a number")

    try:
        # Get the json file using my API
        coincap = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6bb100b7f7cd8dcd08a56514d2f7e4464792d6603f9488e4cf6df629e50ba7b3")

        # Decode the new json file
        json_coincap = coincap.json()
        # Look inside the json_coincap dict, and finding the priceUsd variable
        bitcoin_usd_price = float(json_coincap["data"]["priceUsd"])

    except requests.RequestException:
        # Incase the API fails, exit the program
        sys.exit

    # The new total, will be the ammount of bitcoins the user input times the bitcoin price in usd
    total = bitcoins * bitcoin_usd_price
    # Print out on the screen the new value, seperated by 4 decimal places
    print(f"${total:,.4f}")

else:
    # In case the user didnt add any other argument in the command line, exit the program
    sys.exit("Missing command-line argument")
