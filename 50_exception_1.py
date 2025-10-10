#first example of exception handling mechanism 
#write a program to findout strike rate of batter using given runs and ball played. 

#convert runs and ball into integer 
#findout Strike rate 
while True:
    try:
        run = input("Enter runs ")
        ball = input("Enter balls")
        run = int(run)
        ball = int(ball)
        strike_rate = run/ball 
        print("Strike rate is ",strike_rate)
        break #stop loop 
    except ZeroDivisionError as error:
        print("ball can not be zero")
        print(error)
    except ValueError as error:
        print("invalid input, input must be numbers")
        print(error)
print("Good bye")