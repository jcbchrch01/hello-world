Pay = int(input("Please enter your hourly wage: "))
Hours = int(input("Please enter the amount of hours worked: "))
OT = int(input("Please enter your amount of overtime worked: "))
OT = OT * 1.5 * Pay
Total = OT + Hours * Pay
print("You'll be receiving $",Total,"before tax.")
