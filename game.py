import mysql.connector
conn = mysql.connector.connect(host = "localhost",user ="Nonhlanhla", password = "Mbube123@", database = "guessing_game")
c = conn.cursor()


import random
number = random.randint(1,100)
Guess_Number = 0


def add_people(Firstname,Lastname,age,Guess_Number):
    x = "insert into guesses(Firstname,Lastname,age,Guess_Number) values(%s,%s,%s,%s)"
    c.execute(x,(Firstname,Lastname,age,Guess_Number))
    conn.commit()
    
    if Guess_Number < number:
        print("Guess Higher")

    elif Guess_Number > number:
        print("Guess lower")
    else:
        print("Correct")

    
 


def main():
    while True:
        try:
            user = int(input("Press 1 to to join the Game , Press 0 to Exit: "))

            if user ==1:
                Firstname = input("Enter your Name: ")
                Lastname = input("Enter your Last Name:")
                age = int(input("Enter your Age: "))
                Guess_Number = int(input("Enter your Guess Number: "))
                add_people(Firstname,Lastname,age,Guess_Number)
            
            elif user ==0:
                print("Exited the Game")
                break

        except ValueError:
            print("Invalid Input")
if __name__ == "__main__":
    main()
c.close()
conn.close()