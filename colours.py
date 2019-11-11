#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program uses a for loop


def main():
    # this function uses a nested loop

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process & output
    for counter1 in range(0,1):
        for counter2 in range(0, 5):
            for counter3 in range(0, 5):
                print("Color {0},{1},{2}".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
