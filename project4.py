BounceIndex = float(input("Please enter the bounce index of the ball: "))
Bounces = float(input("Please enter how many times the ball bounced: "))
Height = float(input("Please enter the height the ball was dropped from: "))

Dist = 0

while Bounces > 0:
    Dist = Dist + Height
    Height = Height * BounceIndex
    Dist = Dist + Height
    Bounces -= 1

print("The ball traveled a total distance of %0.2f" % Dist, "feet.")
