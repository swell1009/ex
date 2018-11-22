# Page64
import turtle  # strongly suggest that the Import statement be written at the beginning

answer = input("Do you want to see a spiral? y/n:")
if answer == 'y':
    print("Working...")
    t = turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x * 2)
        t.left(89)
print("Okay, we're done!")
