#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the sum of sequential numbers starting at 0


def main():
    # this function uses a loop

    # this is to keep track of the loop and calculate the sum
    loop_counter = 0
    total = 0

    # input
    user_input_as_string = input("Enter a positive integer : ")

    # process & output
    try:
        user_input = int(user_input_as_string)
        while loop_counter < user_input:
            loop_counter = loop_counter + 1
            total = total + loop_counter
        else:
            print(
                "The sum of all positive numbers from 1 to {0} is {1}.".format(
                    user_input, total
                )
            )
    except Exception:
        print("Invalid integer entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
