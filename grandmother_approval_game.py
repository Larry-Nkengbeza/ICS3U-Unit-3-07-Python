# 3/usr/bin/env Python3

# This program was created by Larry Nkengbeza
# This program was creaed on December 2020
# This program is a grandmother approval game.


def main():
    # input
    user_input = int(input("Enter your age in numerical value: "))

    # Process and Output
    if user_input == 25 or user_input < 40:
        print("You are eligible to date my granddaughter.")
    else:
        print("you are not eligible to date my granddaughter.")


if __name__ == "__main__":
    main()
