# Description: A simple Python script that does some random stuff as a demo for VCS
# Author: Knivier

@staticmethod
# Define the main function: this is the entry point of the script
def main():
    print("Hello, world!")
    print(intakeInfo())

@staticmethod
def intakeInfo():
    age = input("What is your age? ")
    name = input("What is your name? ")
    return "Hello, " + name + "! You are " + age + " years old."

main() # Call the main function