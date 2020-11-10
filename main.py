# If Else

import turtle

bsk = turtle.Turtle()

guess = int(input("what is 2 * 7"))

if guess == 2*7:
    bsk.write(str(guess) + 'is Correct!')
    bsk.penup()
    bsk.backward(10)
else:
    bsk.write("you said" + str(guess) + '> i got ' + str(2*7))
    bsk.penup()
    bsk.backward(10)