
# A3: Resistor Color Codes

clr = input("Enter band colour: ").strip().lower()
 
if clr == "black":
    digit = 0
elif clr == "brown":
    digit = 1
elif clr == "red":
    digit = 2
elif clr == "orange":
    digit = 3
elif clr == "yellow":
    digit = 4
elif clr == "green":
    digit = 5
elif clr == "blue":
    digit = 6
elif clr == "violet":
    digit = 7
elif clr == "grey":
    digit = 8
elif clr == "white":
    digit = 9
else:
    digit = None
 
if digit is None:
    print("Invalid colour")
else:
    print("Digit =", digit)
