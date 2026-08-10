def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):

    # Removes the $ sign and converts the number into an actual float
    dollars = float(dollars.lstrip("$"))

    # Returns the result to main
    return dollars

def percent_to_float(percent):

    # Removes the % sign, multiplies the value by 0.01 so it becomes an percentage value
    # and converts into an actual float
    percent = float(percent.rstrip("%")) * 0.01

    # Returns the result to main
    return percent

main()
