#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/Jun2/2021
# this program generates 10 random numbers between 1 and 100
# then calculates the average of the numbers and display it


import random


def main():
    # this function uses an array
    random_number = []
    # start
    print("Starting ...")
    # input
    for loop_counter in range(0, 10):
        random_ = random.randint(1, 100)
        random_number.append(random_)
        # output
        print(
            "\nThe random number is: {0}"
            .format(random_number[loop_counter]), end="")
    # process
    average = sum(random_number) / 10
    # output
    print("\n\nThe average is {0}".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
