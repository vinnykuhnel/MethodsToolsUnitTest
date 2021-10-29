import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    if num2 != 0:
        return float(num1) /float(num2)

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        test = temp[::-1]

        if(test == temp):
            return True

        else:
            return False
    except:
        print("This is not a valid input")
        return False


## has input to receive two numbers
## divides the two, then outputs the result
def divide():

    num1 = int(input("Enter a number: "))

    num2 = int(input("Enter another number: "))


    if num2 != 0:
        div = float(num1) /float(num2)



    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):
    try:
        return math.sqrt(num)
    except:
        print("This is not an allowed value for num")


## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    if numbers and (len(numbers) + 1) > abs(index): 
        print("Your item at", index, "index is", numbers[index])
