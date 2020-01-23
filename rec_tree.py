"""Modify the recursive tree program using one or all of the following ideas:

Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.

Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.

Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.

Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

If you implement all of the above ideas you will have a very realistic looking tree. """

import turtle
import random

def wid(branchLen):
    if branchLen >50:
        return 10
    elif branchLen>25:
        return 5
    else:
        return 2

def tree(branchLen,t):
    if branchLen > 5:
        x=wid(branchLen)
        t.pensize(x)
        t.forward(branchLen)
        rightangle=random.randrange(15,45)
        lenchg=random.randrange(10,20)
        t.right(rightangle)
        tree(branchLen-lenchg,t)
        leftangle=random.randrange(15,45)
        lenchg=random.randrange(10,20)
        t.left(rightangle+leftangle)
        tree(branchLen-15,t)
        t.right(leftangle)
        t.backward(branchLen)

def main():
    t=turtle.Turtle()
    w=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")

    tree(75,t)
    w.exitonclick()
main()



