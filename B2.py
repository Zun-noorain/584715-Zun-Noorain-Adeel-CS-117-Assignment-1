
# B2: Resistors in Series

qty = int(input("How many Resistors? "))

R_total = 0
 
for i in range(1, qty + 1):

    R = float(input("Enter R" + str(i) + ": "))

    R_total = R_total + R
 
print("Total Resistance =", R_total, "ohm")
