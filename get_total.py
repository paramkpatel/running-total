"""
Author:  Param Patel

Language:  Python 3

To Run: ~$ python3 get_total.py

Purpose: Was bored and I had to count the total of a set of
numbers which consisted of approximately 50 lines. To simplify the process
and avoid manual calculation, I created a program that accepts a text file
as input and automatically adds up all the numbers contained within it. In
addition, I have included a sample text file to demonstrate the proper
formatting required for the program to accurately compute the total.

Bugs: None so far. But if you find any bugs let me know! :-)
"""


def main():
    global file_name
    try:
        file_name = input("Text file to calculate: ")
        sc = open(file_name, "r")
        contents = []
        for i in sc:
            check = i.strip()
            contents.append(check)
        total_amount = 0
        for nums in contents:
            total_amount = float(nums) + total_amount
        print(f"\nThe total of this year was: {round(total_amount, 2):,}\n")
    except FileNotFoundError:
        print(f"\n File \"{file_name}\" is not in the same directory or"
              f" does not exist.")


if __name__ == '__main__':
    main()
