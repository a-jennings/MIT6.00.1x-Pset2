# Paste your code into this box
#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between
#0 (inclusive) and 100 (not inclusive). The computer makes guesses,
#and you give it input - is its guess too high or too low?
#Using bisection search, the computer will guess the user's secret number!

#number = int(input
print("Please think of a number between 0 and 100")
high = 100
low = 0

attempts = 0

while True:
    guess = int((high+low)/2)
    attempts += 1
    user_in = input("Is your secret number " +str(guess) + "? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_in == 'h':
        high = guess
    elif user_in == 'l':
        low = guess
    elif user_in == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        continue
