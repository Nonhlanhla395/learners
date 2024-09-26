import mysql.connector 
conn = mysql.connector.connect(host="localhost",user="Nonhlanhla",password="Mbube123@")
c = conn.cursor()
c.execute("create databases(game)")
conn.commit()

import random
number = random.randint(1,100)
guess = 0


def add_people(person_name,age,guess):
    x = "insert into guesses(person_name,age,guess) values(%s,%s,%s)"
    c.execute(x,(person_name,age,guess))
    conn.commit()
    
    if guess < number:
        print("Guess Higher")

    elif guess > number:
        print("Guess lower")
    else:
        print("Correct")

    
 


def main():
    while True:
        try:
            user = int(input("Press 1 to to join the Game , Press 0 to Exit: "))

            if user ==1:
                person_name = input("Enter your Name: ")
                age = int(input("Enter your Age: "))
                guess = int(input("Enter your Guess Number: "))
                add_people(person_name,age,guess)
            
            elif user ==0:
                print("Exited the Game")
                break

        except ValueError:
            print("Invalid Input")
if __name__ == "__main__":
    main()
c.close()
conn.close()