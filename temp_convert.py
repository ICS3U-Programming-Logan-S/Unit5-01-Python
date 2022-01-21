# Created by: Logan S
# Created on: Jan 20, 2022
# This program converts Celsius temperatures to Fahrenheit temperatures.


def fahrenheit():

    # user input
    temp_c = input("Enter the amount temperature (Celsius): ")

    # Error check
    try:
        temp_c_float = float(temp_c)
        temp_f = (9/5) * (temp_c_float) + 32
        print("The temperature from Celsuis to Fahrenheit is {:.1f}°F!"
              .format(temp_f))
    except Exception:
        print("Invalid input, Please Try again!")
        fahrenheit()


def main():

    # calls function
    fahrenheit()


if __name__ == "__main__":
    main()
