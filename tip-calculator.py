# This is a tip calculator. It asks for the total bill, the tip percentage, and the number of people
# to split the bill. It then calculates the amount each person should pay.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
ppl = int(input("How many people to split the bill? "))

payout = round((bill / ppl) + ((bill / ppl) * (tip / 100)), 2)
print("Each person should pay: ", payout)
