import mysql.connector
conn = mysql.connector.connect(host = "localhost",user ="Nonhlanhla", password = "Mbube123@",database="game_guessing")
c = conn.cursor()

import random
number = random.randint(0,100)
guess = 0

def join(person_name,age,guess):
    x = "insert into guessing(person_name,age,guess) values(%s,%s,%s)"
    c.execute(x,(person_name,age,guess))
    conn.commit()

    if guess > number:
        print("Guess Lower")
    elif guess < number:
        print("Guess Higher")
    else:
        print("Congra You are Correct")

def main():
    while True:
        try:
            user = int(input("Press 1 to join Jelly Game, Press 0 to exit the Game: "))

            if user == 1:
                person_name = input("Enter your Name: ")
                age = int(input("Enter your Age: "))
                guess = int(input("Enter your Guess Number: "))
                join(person_name,age,guess)

            elif user == 0:
                print("You have Exited the Jelly Game")
                break

        except ValueError:
            print("Invalid Input")

if __name__ == "__main__":
    main()

c.close()
conn.close()